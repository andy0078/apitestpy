# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 14:13
# @Copyright：北京码同学
import os
import sys

import pytest

from common.file_load import load_yaml_file, write_yaml

if __name__ == '__main__':
    # 获取外部传参
    args = sys.argv
    # print(args)
    env_file_path = '/config/env_test.yml'
    if len(args) > 1:
        env_name = args[1]  # 得到传入的环境名称
        env_file_path = f'/config/env_{env_name}.yml'  # 拼接环境配置文件路径
        del args[1]
    # 得到环境名称去读对应的环境信息配置文件
    env_info = load_yaml_file(env_file_path)
    # 获取到环境信息之后，将他们分别写http.yml,common.yml,redis.yml,db.yml
    write_yaml('/config/common.yml', env_info['common'])
    write_yaml('/config/http.yml', env_info['http'])
    write_yaml('/config/redis.yml', env_info['redis'])
    write_yaml('/config/db.yml', env_info['db'])
    # 执行时，会自动识别pytest.ini中的规则，完成执行
    # pytest -sv  --alluredir ./report/data --clean-alluredir testcases
    # os.system('allure generate ./report/data -o ./report/html --clean')
