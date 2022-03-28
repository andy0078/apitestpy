# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-13 11:43
# @Copyright：北京码同学
from api.base_api import BaseBasicApi
from setting import DIR_NAME


class UploadFileApi(BaseBasicApi):

    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/uploaders'
        self.method = 'post'
        self.files = {
            # 'logo.png' 文件名称
            # open(r'C:\Users\lixio\Desktop\logo.png',mode='rb')  读取文件二进制对象
            # 'image/png' 文件类型
            'file': ('logo.png', open(DIR_NAME + '/data/logo.png', mode='rb'), 'image/png')
        }
        self.params = {
            'scene': 'goods'
        }


if __name__ == '__main__':
    resp = UploadFileApi().send()
    print(resp.status_code)
    print(resp.json())
