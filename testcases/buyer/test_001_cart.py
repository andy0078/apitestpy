# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 15:57
# @Copyright：北京码同学
import allure
import pytest

from  api.buyer.cart import AddCartApi, BuyNowApi
from  common.file_load import read_excel


@allure.feature('购物车接口')
class TestAddCart:
    # test_data = [
    #     ['必填参数均正确没有非必填字段',5173,   1,       200,'',''],
    #     ['产品已下架',               5875,   1,      500,'004','产品已下架'],
    #     ['产品不存在',              456665,  1,      500,'451','商品已失效，请刷新购物车'],
    #     ['购买数量超过库存',           5173, 99999999, 500,'451','商品库存已不足，不能购买。'],
    #     ['购买数量为0',               5173,  0,        400,'004','加入购物车数量必须大于0'],
    #     ['购买数量为负数',             5173,   -1,     400,'004','加入购物车数量必须大于0'],
    #     ['购买数量为空',               5173,  None,    400,'004','购买数量不能为空'],
    #     ['产品id为空',                None,      1,    400,'004','产品id不能为空']
    # ]
    test_data = read_excel('/data/mtxshop_testdata.xlsx', '添加购物车')

    @allure.story('添加购物车接口异常测试')
    @allure.title('{casename}')
    @pytest.mark.parametrize('casename,sku_id,num,expect_status_code,expect_busi_code,expect_message', test_data)
    def test_add_cart(self, casename, sku_id, num, expect_status_code, expect_busi_code, expect_message):
        # 调用接口，传入测试数据
        add_cart = AddCartApi(sku_id=sku_id, num=num)
        resp = add_cart.send()
        status_code = resp.status_code
        assert status_code == expect_status_code
        print(resp.text)  # 由于响应信息可能为空，所以我们使用resp.text打印结果，因为空的字符串是无法使用resp.json()去获取的
        # 注意这个接口如果业务正常成功，那么响应信息是空的
        if status_code != 200:
            # 状态码不是200时，才进行响应信息的校验
            try:
                resp_json = resp.json()
            except:
                pass
            code = resp_json['code']
            # assert code == expect_busi_code

            pytest.assume(code == expect_busi_code.replace('"', ''))
            # 判断message的值是 商品已失效，请刷新购物车
            message = resp_json['message']
            # assert message == expect_message
            pytest.assume(message == expect_message)


@allure.feature('购物车接口')
class TestBuyNow:
    test_data = read_excel('/data/mtxshop_testdata.xlsx', '立即购买')

    @allure.story('立即购买接口异常测试')
    @allure.title('{casename}')
    @pytest.mark.parametrize('casename,sku_id,num,expect_status_code,expect_busi_code,expect_message', test_data)
    def test_buy_now(self, casename, sku_id, num, expect_status_code, expect_busi_code, expect_message):
        # 调用接口，传入测试数据
        add_cart = BuyNowApi(sku_id=sku_id, num=num)
        resp = add_cart.send()
        status_code = resp.status_code
        assert status_code == expect_status_code
        print(resp.text)  # 由于响应信息可能为空，所以我们使用resp.text打印结果，因为空的字符串是无法使用resp.json()去获取的
        # 注意这个接口如果业务正常成功，那么响应信息是空的
        if status_code != 200:
            # 状态码不是200时，才进行响应信息的校验
            try:
                resp_json = resp.json()
            except:
                pass
            code = resp_json['code']
            # assert code == expect_busi_code

            pytest.assume(code == expect_busi_code.replace('"', ''))
            # 判断message的值是 商品已失效，请刷新购物车
            message = resp_json['message']
            # assert message == expect_message
            pytest.assume(message == expect_message)
