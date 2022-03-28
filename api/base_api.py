# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 14:55
# @Copyright：北京码同学
import requests

from  common.client import RequestsClient
from  common.file_load import load_yaml_file


class BaseBuyerApi(RequestsClient):
    # session = requests.session()
    buyer_token = ''

    def __init__(self):
        super().__init__()
        self.host = load_yaml_file('/config/http.yml')['buyer']
        # self.session = BaseBuyerApi.session
        # self.url = None
        # self.method = None
        self.headers = {
            'Authorization': BaseBuyerApi.buyer_token
        }
        # self.params = None
        # self.data = None
        # self.json = None
        # self.files = None
        # self.resp = None

    # def send(self,**kwargs):
    #     # 抽取时，每个接口的request请求不一定会发送多少个参数
    #     # 可以使用不定长关键字参数传递方式
    #     # 判断一下，调用send时，如果有些参数没有传，那么就用对象自身的
    #     if 'url' not in kwargs:
    #         kwargs['url'] = self.url
    #     if 'method' not in kwargs:
    #         kwargs['method'] = self.method
    #     if 'headers' not in kwargs:
    #         kwargs['headers'] = self.headers
    #     if 'params' not in kwargs:
    #         kwargs['params'] = self.params
    #     if 'data' not in kwargs:
    #         kwargs['data'] = self.data
    #     if 'json' not in kwargs:
    #         kwargs['json'] = self.json
    #     if 'files' not in kwargs:
    #         kwargs['files'] = self.files
    #     self.resp = self.session.request(**kwargs)
    #     return self.resp


class BaseSellerApi(RequestsClient):
    seller_token = ''

    def __init__(self):
        super().__init__()
        self.host = load_yaml_file('/config/http.yml')['seller']
        self.headers = {
            'Authorization': BaseSellerApi.seller_token
        }


class BaseManagerApi(RequestsClient):
    manager_token = ''

    def __init__(self):
        super().__init__()
        self.host = load_yaml_file('/config/http.yml')['manager']
        self.headers = {
            'Authorization': BaseManagerApi.manager_token
        }


class BaseBasicApi(RequestsClient):
    def __init__(self):
        super().__init__()
        self.host = load_yaml_file('/config/http.yml')['basic']
