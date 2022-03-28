# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-13 14:31
# @Copyright：北京码同学
import time

import allure
import jsonpath
import pytest

from apiframework.api.buyer.cart import BuyNowApi, DeleteCartApi, AddCartApi
from apiframework.api.buyer.comment import CommentApi
from apiframework.api.buyer.create_trade import CreateTradeApi
from apiframework.api.buyer.orders import ConfirmOrgApi
from apiframework.api.seller.order import OrderDeliveryApi, OrderPayApi
from apiframework.common.file_load import read_excel


@allure.feature('订单流程测试')
class TestOrderProcess:
    order_sn = ''
    pay_price = 0
    sku_id = ''
    # 买家下单
    test_data = read_excel('/data/mtxshop_testdata.xlsx', '创建交易')

    @allure.story('创建交易正常业务')
    @allure.title('{casename}')
    @pytest.mark.parametrize('casename,client,way,expect_statuscode', test_data)
    def test_create_trade(self, casename, client, way, expect_statuscode, get_goods):
        goods_id = get_goods[0]
        TestOrderProcess.sku_id = get_goods[1]
        # 创建交易需要调用立即购买接口或者添加购物车接口来提供数据
        if way == 'BUY_NOW':
            # 需要sku_id，不能写死，数据从哪里来
            BuyNowApi(sku_id=TestOrderProcess.sku_id, num=1).send()
        elif way == 'CART':
            # 清空购物车
            DeleteCartApi().send()
            AddCartApi(sku_id=TestOrderProcess.sku_id, num=1).send()
        resp = CreateTradeApi(client=client, way=way).send()
        pytest.assume(resp.status_code == 200)
        resp_json = resp.json()
        TestOrderProcess.order_sn = jsonpath.jsonpath(resp_json, '$..sn')[0]
        TestOrderProcess.pay_price = jsonpath.jsonpath(resp_json, '$..total_price')[0]

    # 卖家发货
    @allure.title('卖家发货接口')
    def test_delivery(self, db_util):
        time.sleep(1)
        resp = OrderDeliveryApi(order_sn=TestOrderProcess.order_sn).send()
        pytest.assume(resp.status_code == 200)
        # 断言订单状态发生变化
        db_res = db_util.select(
            f'SELECT order_status FROM mtxshop_trade.es_order WHERE trade_sn={TestOrderProcess.order_sn};')
        db_order_status = db_res[0]['order_status']
        pytest.assume(db_order_status == 'SHIPPED')

    # 买家收货
    @allure.title('买家收货接口')
    def test_org(self):
        time.sleep(1)
        resp = ConfirmOrgApi(order_sn=TestOrderProcess.order_sn).send()
        pytest.assume(resp.status_code == 200)

    # 卖家收款
    @allure.title('卖家收款接口')
    def test_confirm_pay(self):
        time.sleep(1)
        resp = OrderPayApi(order_sn=TestOrderProcess.order_sn, pay_price=TestOrderProcess.pay_price).send()
        pytest.assume(resp.status_code == 200)

    # 买家评论
    @allure.title('买家评论接口')
    def test_comment(self):
        time.sleep(1)
        resp = CommentApi(order_sn=TestOrderProcess.order_sn, sku_id=TestOrderProcess.sku_id).send()
        pytest.assume(resp.status_code == 200)
