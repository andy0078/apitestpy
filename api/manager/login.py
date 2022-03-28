# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 14:45
# @Copyright：北京码同学
from  api.base_api import BaseManagerApi
from  common.encry_decry import md5
from  common.file_load import load_yaml_file


class ManagerLogin(BaseManagerApi):

    def __init__(self):
        super().__init__()
        self.common = load_yaml_file('/config/common.yml')
        self.url = f'{self.host}/admin/systems/admin-users/login'
        self.method = 'get'
        self.params = {
            'username': self.common['managerName'],
            'password': md5(self.common['managerPassword']),
            'captcha': self.common['captcha'],
            'uuid': 'jsjdhdhdhdhdhdhh'
        }