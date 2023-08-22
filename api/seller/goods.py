# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-13 10:53
# @Copyright：北京码同学
from api.base_api import BaseSellerApi


class AddGoodsApi(BaseSellerApi):

    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/seller/goods'
        self.method = 'post'
        self.json = {
            "brand_id": "",
            "category_id": 83,
            "category_name": "",
            "goods_name": "沙陌炒锅测试商品",
            "sn": "sn000282",
            "price": "280",
            "mktprice": "300",
            "cost": "50",
            "weight": "2",
            "goods_gallery_list": [{
                "img_id": -1,
                "original": "http://www.mtxshop.com:7000/statics/attachment/goods/2022/3/13/10/57184862.png",
                "sort": 0
            }],
            "quantity": 99999999,
            "goods_transfee_charge": 1,
            "has_changed": 0,
            "market_enable": 1,
            "template_id": 0,
            "exchange": {
                "category_id": "",
                "enable_exchange": 0,
                "exchange_money": 0,
                "exchange_point": 0
            },
            "shop_cat_id": 0,
            "meta_description": "",
            "meta_keywords": "",
            "page_title": "",
            "goods_params_list": [],
            "sku_list": [],
            "intro": "商品说明"
        }


class UpdateGoodsApi(BaseSellerApi):

    def __init__(self, goods_id):
        super().__init__()
        self.url = f'{self.host}/seller/goods/{goods_id}'
        self.method = 'put'
        self.json = {
            "goods_id": goods_id,
            "category_id": 83,
            "category_name": "厨房用品&gt;锅具水壶 &gt;炒锅",
            "shop_cat_id": 0,
            "brand_id": None,
            "goods_name": "沙陌炒锅**商品",
            "sn": "sn000282",
            "price": 280,
            "cost": 50,
            "mktprice": "301",
            "weight": 2,
            "goods_transfee_charge": 1,
            "intro": "<p>商品说明</p>",
            "have_spec": 0,
            "quantity": 99999999,
            "market_enable": 1,
            "goods_gallery_list": [{
                "img_id": 9818,
                "original": "http://www.mtxshop.com:7000/statics/attachment/goods/2022/3/13/10/57184862.png",
                "sort": None
            }],
            "page_title": "沙陌炒锅测试商品",
            "meta_keywords": "沙陌炒锅测试商品",
            "meta_description": "沙陌炒锅测试商品",
            "template_id": 0,
            "is_auth": 0,
            "enable_quantity": 99999999,
            "auth_message": None,
            "goods_type": "NORMAL",
            "exchange": {
                "category_id": "",
                "enable_exchange": 0,
                "exchange_money": 0,
                "exchange_point": 0
            },
            "category_ids": [79, 80, 83],
            "promotion_tip": "",
            "sku_list": [],
            "has_changed": 0
        }


class GoodsUnderApi(BaseSellerApi):

    # 由于下架商品的goods_id可以同时传多个，所以我们要设计一下传参方式并且处理
    # 要求传一个列表，这个列表里放的是每个要下架的商品id,['7466','7465'],变成'7466,7465'
    def __init__(self, goods_ids):
        super().__init__()
        goods_ids = ','.join(goods_ids)
        self.url = f'{self.host}/seller/goods/{goods_ids}/under'
        self.method = 'put'
        self.params = {
            'reason': ''
        }


class DeleteGoodsApi(BaseSellerApi):

    # 由于删除商品的goods_id可以同时传多个，所以我们要设计一下传参方式并且处理
    # 要求传一个列表，这个列表里放的是每个要下架的商品id,['7466','7465'],变成'7466,7465'
    def __init__(self, goods_ids):
        super().__init__()
        goods_ids = ','.join(goods_ids)
        self.url = f'{self.host}/seller/goods/{goods_ids}'
        self.method = 'delete'


class GetGoodsSkuInfoApi(BaseSellerApi):

    def __init__(self, goods_id):
        super().__init__()
        self.url = f'{self.host}/seller/goods/{goods_id}/skus'
        self.method = 'get'


if __name__ == '__main__':
    goods_ids = ['7466', '7465']
    print(','.join(goods_ids))
