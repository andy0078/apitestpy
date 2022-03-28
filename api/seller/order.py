# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-13 11:28
# @Copyright：北京码同学
from apiframework.api.base_api import BaseSellerApi


class OrderDeliveryApi(BaseSellerApi):

    def __init__(self,order_sn):
        super().__init__()
        self.url = f'{self.host}/seller/trade/orders/{order_sn}/delivery'
        self.method = 'post'
        self.params = {
            'ship_no':'assdfddfg',
            'logi_id':12,
            'logi_name':'中通'
        }
class OrderPayApi(BaseSellerApi):

    def __init__(self,order_sn,pay_price):
        super().__init__()
        self.url = f'{self.host}/seller/trade/orders/{order_sn}/pay'
        self.method = 'post'
        self.params = {
            'pay_price':pay_price
        }