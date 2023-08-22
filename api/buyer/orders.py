# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-13 10:30
# @Copyright：北京码同学
from api.base_api import BaseBuyerApi


class CancelOrderApi(BaseBuyerApi):

    def __init__(self, order_sn):
        super().__init__()
        self.url = f'{self.host}/trade/orders/{order_sn}/cancel'
        self.method = 'post'
        self.params = {
            'reason': '这是取消原因，我啥也不管'
        }


class ConfirmOrgApi(BaseBuyerApi):

    def __init__(self, order_sn):
        super().__init__()
        self.url = f'{self.host}/trade/orders/{order_sn}/rog'
        self.method = 'post'


class ReturnGoodsApi(BaseBuyerApi):

    def __init__(self, order_sn, sku_id):
        super().__init__()
        self.url = f'{self.host}/after-sales/apply/return/goods'
        self.method = 'post'
        self.params = {
            'service_type': 'RETURN_GOODS',
            'return_num': 1,
            'ship_addr': '北京市昌平区回龙观国风美唐',
            'ship_name': 'shamonew',
            'ship_mobile': '15510496222',
            'account_type': 'WEIXINPAY',
            'return_account': 'dfdfffdff',
            'reason': '商品降价',
            'problem_desc': '就是不想要了，没啥原因',
            'order_sn': order_sn,
            'sku_id': sku_id,
            'apply_vouchers': '',
            'region': 2799
        }
