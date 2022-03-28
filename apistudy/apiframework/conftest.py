# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 14:04
# @Copyright：北京码同学
from typing import List

import pytest

from apiframework.api.base_api import BaseBuyerApi, BaseSellerApi, BaseManagerApi
from apiframework.api.buyer.login import BuyerLogin
from apiframework.api.manager.goods import AuditGoodsApi
from apiframework.api.manager.login import ManagerLogin
from apiframework.api.seller.goods import AddGoodsApi, GetGoodsSkuInfoApi, GoodsUnderApi, DeleteGoodsApi
from apiframework.api.seller.login import SellerLogin
from apiframework.common.db_util import DB_Util
from apiframework.common.file_load import load_yaml_file
from apiframework.common.redis_util import RedisUtil


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
@pytest.fixture(scope='session',autouse=True)
def get_seller_token():
    seller_login = SellerLogin()
    resp = seller_login.send()
    BaseSellerApi.seller_token = resp.json()['access_token']
@pytest.fixture(scope='session',autouse=True)
def get_manager_token():
    manager_login = ManagerLogin()
    resp = manager_login.send()
    BaseManagerApi.manager_token = resp.json()['access_token']

# 这个是用来提供已经审核通过的产品信息的
@pytest.fixture(scope='class')
def get_goods():
    # 创建商品
    add_goods_api = AddGoodsApi()
    resp = add_goods_api.send()
    goods_id = resp.json()['goods_id']
    # 管理员审核商品
    # 审核商品需要goods id组成的列表
    audit_goods_api = AuditGoodsApi([goods_id])
    resp = audit_goods_api.send()
    resp = GetGoodsSkuInfoApi(goods_id).send()
    sku_id = resp.json()[0]['sku_id']
    yield goods_id,sku_id # 返回多个值时结果是个元组 (7473,7399)
    # 后置处理，清除该条商品
    GoodsUnderApi([str(goods_id)]).send()#先下架
    DeleteGoodsApi([str(goods_id)]).send()

@pytest.fixture(scope='session',autouse=True)
def redis_util():
    redis_info = load_yaml_file('/config/redis.yml')['mtxshop']
    redis_util = RedisUtil(host=redis_info['host'],pwd=redis_info['password'])
    yield redis_util

@pytest.fixture(scope='session',autouse=True)
def db_util():
    db_info = load_yaml_file('/config/db.yml')['mtxshop']
    db_util = DB_Util(host=db_info['host'], user=db_info['username'], password=db_info['password'])
    yield db_util
    db_util.close()

