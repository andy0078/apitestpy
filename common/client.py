# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 15:21
# @Copyright：北京码同学
import requests

from apiframework.common.encry_decry import AesEncrypt
from apiframework.common.logger import GetLogger


class RequestsClient:
    session = requests.session()  # 统一的一个session对象，可以帮我们自动关联cookie

    def __init__(self):
        self.aes = AesEncrypt('0123456789123456')  # 统一性加密时
        self.logger = GetLogger.get_logger()
        self.session = RequestsClient.session
        self.url = None
        self.method = None
        self.headers = None
        self.params = None
        self.data = None
        self.json = None
        self.files = None
        self.resp = None

    def send(self, **kwargs):
        # 抽取时，每个接口的request请求不一定会发送多少个参数
        # 可以使用不定长关键字参数传递方式
        # 判断一下，调用send时，如果有些参数没有传，那么就用对象自身的
        if 'url' not in kwargs:
            kwargs['url'] = self.url
        if 'method' not in kwargs:
            kwargs['method'] = self.method
        if 'headers' not in kwargs:
            kwargs['headers'] = self.headers
        if 'params' not in kwargs:
            # self.params = self.aes.encrypt(self.params) #加密数据
            kwargs['params'] = self.params
        if 'data' not in kwargs:
            # self.data = self.aes.encrypt(self.data)  # 加密数据
            kwargs['data'] = self.data
        if 'json' not in kwargs:
            # # self.json = self.aes.encrypt(self.json)  # 加密数据
            kwargs['json'] = self.json
        if 'files' not in kwargs:
            kwargs['files'] = self.files
        # 遍历kwargs,收集接口请求的所有信息
        for key, value in kwargs.items():
            self.logger.debug(f'接口的{key}是:{value}')
        try:
            self.resp = self.session.request(**kwargs)
            self.logger.debug(f'接口的响应状态码是:{self.resp.status_code}')
            self.logger.debug(f'接口的响应是:{self.resp.text}')
        except:
            self.logger.exception('接口发起异常')
        return self.resp

    def get_resp_info(self):
        # info = self.aes.decrypt(self.resp.text) #响应信息解密时
        # return info
        return self.resp.text
