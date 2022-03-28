# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 15:47
# @Copyright：北京码同学
from apiframework.api.base_api import BaseBuyerApi


class SetAddressApi(BaseBuyerApi):

    def __init__(self,address_id):
        super().__init__()
        self.url = f'{self.host}/trade/checkout-params/address-id/{address_id}'
        self.method = 'post'

class SetPayTypeApi(BaseBuyerApi):

    def __init__(self,payment_type='COD'):
        super().__init__()
        self.url = f'{self.host}/trade/checkout-params/payment-type'
        self.method = 'post'
        self.params = {
            'payment_type':payment_type
        }

class SetOrderMarkApi(BaseBuyerApi):
    def __init__(self,remark='这是订单备注'):
        super().__init__()
        self.url = f'{self.host}/trade/checkout-params/remark'
        self.method = 'post'
        self.params = {
            'remark':remark
        }
