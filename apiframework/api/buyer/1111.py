# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 15:09
# @Copyright：北京码同学
from apiframework.api.base_api import BaseBuyerApi
from apiframework.api.buyer.cart import AddCartApi
from apiframework.api.buyer.login import BuyerLogin

if __name__ == '__main__':
    buyer_login = BuyerLogin()
    resp = buyer_login.send()
    BaseBuyerApi.buyer_token = resp.json()['access_token']
    add_cart = AddCartApi(sku_id=5173,num=1)
    resp = add_cart.send()
    print(resp.json())
