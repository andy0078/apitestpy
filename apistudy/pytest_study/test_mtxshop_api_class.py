# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-27 11:18
# @Copyright：北京码同学
from apistudy0306.apistudy.requests_study.mtxshop_api import *

def setup_module():
    print('这是模块级别的前置')
def teardown_module():
    print('这是模块级别的后置')

class TestBuyNow():
    # 在类下面去编写测试脚本
    # 以一个方法作为一个测试用例，方法的默认规则是test_开头或者_test结尾
    def setup_class(self):
        buyer_login()
        print('当前类下用例执行之前，只执行一次')
    def teardown_class(self):
        print('当前类下用例执行之后，只执行一次')
    def setup_method(self):
        print('当前类下每条用例执行之前，执行一次')
    def teardown_method(self):
        print('当前类下每条用例执行之后，执行一次')
    def test_buy_now(self):
        # buyer_login()
        resp = buy_now()
        # 做断言
        status_code = resp.status_code
        assert status_code == 200
    def test_buy_now1(self):
        # buyer_login()
        resp = buy_now(sku_id=6354535)
        # 做断言
        status_code = resp.status_code
        print(resp.json())
        assert status_code == 500
        # {'code': '004', 'message': '不合法'}
        resp_json = resp.json()
        code = resp_json['code']
        assert code == '004'
        # 判断message的值是 商品已失效，请刷新购物车
        message = resp_json['message']
        assert message == '不合法'
