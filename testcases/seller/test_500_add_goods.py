# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-13 15:29
# @Copyright：北京码同学
import allure
import pytest

from api.seller.goods import AddGoodsApi
from common.file_load import read_excel


@allure.feature('卖家添加商品接口')
class TestAddGoods:
    test_data = read_excel('/data/mtxshop_testdata.xlsx', '添加商品')

    @allure.story('卖家添加商品接口异常测试')
    @allure.title('{casename}')
    @pytest.mark.parametrize('casename,jsonparams,expect_stauscode', test_data)
    def test_add_goods(self, casename, jsonparams, expect_stauscode):
        jsonparams = eval(jsonparams)  # 由于从excel读出的json参数是一个字符串，所以我们将其转换字典
        add_goods_api = AddGoodsApi()
        add_goods_api.json = jsonparams  # 给接口的json属性重新赋值，值为为excel读出的数据
        resp = add_goods_api.send()
        assert resp.status_code == expect_stauscode
