# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 14:04
# @Copyright：北京码同学
from typing import List

import pytest

from apiframework.api.base_api import BaseBuyerApi
from apiframework.api.buyer.login import BuyerLogin

def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")




# 获取token
@pytest.fixture(scope='session',autouse=True)
def get_buyer_token():
    buyer_login = BuyerLogin()
    resp = buyer_login.send()
    BaseBuyerApi.buyer_token = resp.json()['access_token']