# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 14:45
# @Copyright：北京码同学
import requests

from  api.base_api import BaseBuyerApi
from  common.encry_decry import md5
from  common.file_load import load_yaml_file


class BuyerLogin(BaseBuyerApi):

    def __init__(self):
        super().__init__()
        self.common = load_yaml_file('/config/common.yml')
        self.url = f'{self.host}/passport/login'
        self.method = 'post'

        # self.headers = {
        #     'Authorization': ''
        # }
        # 查询参数通常使用params来表示
        self.params = {
            'username': self.common['buyerName'],
            'password': md5(self.common['buyerPassword']),
            'captcha': self.common['captcha'],
            'uuid': 'jsjdhdhdhdhdhdhh'
        }
    # def send(self):
    #     resp = requests.session().request(url=self.url, method='post', headers=self.headers, params=self.params)
    #     return resp