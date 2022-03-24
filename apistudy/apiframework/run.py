# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 14:13
# @Copyright：北京码同学
import os

import pytest

if __name__ == '__main__':
    # 执行时，会自动识别pytest.ini中的规则，完成执行
    pytest.main() # pytest -sv  --alluredir ./report/data --clean-alluredir testcases
    os.system('allure generate ./report/data -o ./report/html --clean')