# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-27 11:41
# @Copyright：北京码同学
import json

import javaobj
import pytest

from apistudy0306.apistudy.requests_study.mtxshop_api import *
@pytest.mark.usefixtures('ceshilei')
class TestBuyNowDataDriver:

    # def setup_class(self):
    #     buyer_login()
    # 测试数据管理对象
    test_data = [
        ['必填参数均正确没有非必填字段',5173,   1,       200,'',''],
        ['产品已下架',               5875,   1,      500,'004','产品已下架'],
        ['产品不存在',              456665,  1,      500,'004','不合法'],
        ['购买数量超过库存',           5173, 99999999, 500,'451','商品库存已不足，不能购买。'],
        ['购买数量为0',               5173,  0,        400,'004','购买数量必须大于0'],
        ['购买数量为负数',             5173,   -1,     400,'004','购买数量必须大于0'],
        ['购买数量为空',               5173,  None,    400,'004','购买数量不能为空'],
        ['产品id为空',                None,      1,    400,'004','产品id不能为空']
    ]
    @pytest.mark.usefixtures('ceshilei') # 这也是一种调用fixture方法的方式，参数是fixture方法的名字
    @pytest.mark.parametrize('casename,sku_id,num,expect_status_code,expect_busi_code,expect_message',test_data)
    def test_buy_now(self,casename,sku_id,num,expect_status_code,expect_busi_code,expect_message,redis_util,get_token):
        # 调用接口时传入测试数据中相关的变量
        resp = buy_now(sku_id=sku_id,num=num)
        # 做断言
        status_code = resp.status_code
        assert status_code == expect_status_code
        print(resp.text) # 由于响应信息可能为空，所以我们使用resp.text打印结果，因为空的字符串是无法使用resp.json()去获取的
        # 注意这个接口如果业务正常成功，那么响应信息是空的
        if status_code!=200:
            # 状态码不是200时，才进行响应信息的校验
            try:
                resp_json = resp.json()
            except:
                pass
            code = resp_json['code']
            # assert code == expect_busi_code
            pytest.assume(code == expect_busi_code)
            # 判断message的值是 商品已失效，请刷新购物车
            message = resp_json['message']
            # assert message == expect_message
            pytest.assume(message == expect_message)
        if status_code == 200:
            # 从redis中获取数据并做校验
            uid = get_token #get_token是个fixture，调用时他就相当于他的返回值，我们返回了uid
            # 格式化字符串时，如果字符串本身就有大括号，那么需要使用双大括号
            res = redis_util.get(f'{{BUY_NOW_ORIGIN_DATA_PREFIX}}_{uid}')
            res_list = javaobj.loads(res)  # 这是得到结果转换成python的列表
            # 业务上这个列表中，只会存储一个数据
            obj = res_list[0]  # 通过索引得到列表里的数据
            redis_num = obj.__getattribute__('num') # 实际结果
            redis_skuId = obj.__getattribute__('skuId') # 实际结果
            pytest.assume(redis_num == num)
            pytest.assume(redis_skuId == sku_id)


class TestCreateTrade:
    # def setup_class(self):
    #     buyer_login()

    client_data = ['PC','WAP','NATIVE','REACT','MINI'] # 5
    way_data = ['BUY_NOW','CART'] # 2
    expect_status_code = [200] # 1
    # 上面三组数据都作为参数，同时组合形成测试数据，组合结果总共5*2*1=10
    # 这种方式叫做 pytest笛卡尔积参数化
    # 笛卡尔积使用场景，在一个接口参数中存在多个参数具备有效值，并且他们需要组合才能覆盖正向场景，就可以使用笛卡尔积
    @pytest.mark.parametrize('client',client_data)
    @pytest.mark.parametrize('way',way_data)
    @pytest.mark.parametrize('expect_status',expect_status_code)
    def test_create_trade(self,client,way,expect_status,db_util):
        # 对于创建交易这个来说，在调用之前需要先调用立即购买或者添加购物车接口
        # 因为创建交易会根据参数的不同去redis缓存中取订单相关的信息，然后创建
        # 当way参数是BUY_NOW会去缓存中读立即购买的数据
        # 当way参数是CART时会去缓存中读添加购物车的数据
        # 如何让缓存中产生创建交易接口需要的数据，就是调用对应的接口
        if way == 'BUY_NOW':
            buy_now()
        elif way == 'CART':
            delete_cart() #先清空购物车，防止多人使用或者购物车里有异常数据
            add_cart()
        resp = create_trade(client=client,way=way)
        status_code = resp.status_code
        print(resp.text)
        assert status_code == expect_status

        # 判断数据数据库数据是否正确
        # 数据库里是实际值，那么期望数据是谁
        # 期望数据可以是接口发起时的接口数据，比如产品id，下单数量
        # 期望数据还可以是接口响应数据里的内容
        data = db_util.select('SELECT * FROM mtxshop_trade.es_order WHERE member_id=59 ORDER BY order_id DESC LIMIT 1 ;')
        db_res = data[0] # 第一行数据，这是个字典
        db_trade_sn = db_res['trade_sn']
        items_json = db_res['items_json']
        # print(type(items_json))  # 由于items_json拿到之后是个字符串，不好从中提取内容
        # 所以我们可以将字符串转换列表套字典的形式
        # items_json = eval(items_json) # 这种不行，因为字符串有null，python里是None
        # print(type(items_json))
        items_json = json.loads(items_json)  # 使用json库需要先导入import json
        print(type(items_json))
        print(items_json)
        print(json.dumps(items_json))
        # print(items_json[0])
        # print(items_json[0]['sku_id'])
        # print(items_json[0]['num'])
        # db_sku_id = items_json[0]['sku_id']
        # db_num = items_json[0]['num']

        db_sku_id = jsonpath.jsonpath(items_json,'$..sku_id')[0]
        db_num = jsonpath.jsonpath(items_json,'$..num')[0]

        # 获取响应信息中的期望值
        resp_json = resp.json()
        resp_trade_sn = resp_json['trade_sn']
        pytest.assume(db_trade_sn == resp_trade_sn) #断言响应数据和数据库中trade_sn是否一致
        pytest.assume(db_sku_id == 5173)
        pytest.assume(db_num == 1)

        # 提取响应中的sn
        print(resp_json['order_list'][0]['sn'])
        # 上述提取比较复杂，我们可以jsonpath表达式来帮我们


