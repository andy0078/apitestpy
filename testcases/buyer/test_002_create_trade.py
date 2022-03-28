# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-13 13:40
# @Copyright：北京码同学
import allure
import pytest

from api.buyer.cart import BuyNowApi, AddCartApi, DeleteCartApi
from api.buyer.create_trade import CreateTradeApi
from apiframeworkmon.file_load import read_excel

@allure.feature('创建交易接口')
class TestCreateTrade:
    test_data = read_excel('/data/mtxshop_testdata.xlsx', '创建交易1')
    @allure.story('创建交易接口异常测试')
    @allure.title('{casename}')
    @pytest.mark.parametrize('casename,client,way,expect_statuscode',test_data)
    def test_create_trade(self,casename,client,way,expect_statuscode):
        # goods_id = get_goods[0]
        # sku_id = get_goods[1]
        # # 创建交易需要调用立即购买接口或者添加购物车接口来提供数据
        # if way == 'BUY_NOW':
        #     # 需要sku_id，不能写死，数据从哪里来
        #     BuyNowApi(sku_id=sku_id,num=1).send()
        # elif way == 'CART':
        #     # 清空购物车
        #     DeleteCartApi().send()
        #     AddCartApi(sku_id=sku_id,num=1).send()
        resp = CreateTradeApi(client=client,way=way).send()
        pytest.assume(resp.status_code == 500)

