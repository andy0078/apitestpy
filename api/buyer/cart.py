# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 14:48
# @Copyright：北京码同学
import requests

from api.base_api import BaseBuyerApi


class AddCartApi(BaseBuyerApi):

    def __init__(self,sku_id,num):
        super().__init__()
        self.url = f'{self.host}/trade/carts'
        self.method = 'post'
        # global token
        # self.headers = {
        #     'Authorization': token
        # }
        # 查询参数通常使用params来表示
        self.params = {
            'sku_id': sku_id,
            'num': num
        }
    # def send(self):
    #     resp = requests.session().request(url=self.url, method='post', headers=self.headers, params=self.params)
    #     return resp

class BuyNowApi(BaseBuyerApi):

    def __init__(self,sku_id,num):
        super().__init__()
        self.url = f'{self.host}/trade/carts/buy'
        self.method = 'post'
        # global token
        # self.headers = {
        #     'Authorization': token
        # }
        # 查询参数通常使用params来表示
        self.params = {
            'sku_id': sku_id,
            'num': num
        }
    # def send(self):
    #     resp = requests.session().request(url=self.url, method='post', headers=self.headers, params=self.params)
    #     return resp
class DeleteCartApi(BaseBuyerApi):

    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/trade/carts'
        self.method = 'delete'
        # global token
        # self.headers = {
        #     'Authorization': token
        # }
        # self.headers['Content-Type'] = 'application/json'
    # def send(self):
    #     resp = requests.session().request(url=self.url, method='delete', headers=self.headers)
    #     return resp