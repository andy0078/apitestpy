# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 14:45
# @Copyright：北京码同学
import requests

from apiframework.api.base_api import BaseBuyerApi


class BuyerLogin(BaseBuyerApi):

    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/passport/login'
        self.method = 'post'

        # self.headers = {
        #     'Authorization': ''
        # }
        # 查询参数通常使用params来表示
        self.params = {
            'username': 'shamo',
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'captcha': '1512',
            'uuid': 'jsjdhdhdhdhdhdhh'
        }
    # def send(self):
    #     resp = requests.session().request(url=self.url, method='post', headers=self.headers, params=self.params)
    #     return resp