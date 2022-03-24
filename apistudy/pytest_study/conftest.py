# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-27 14:34
# @Copyright：北京码同学
from typing import List

# 注意这是pytest内置的一个钩子函数
# 在执行时会自动扫描该文件，并执行该钩子函数
import pytest

from apistudy0306.apistudy.mysql_study.db_util import DB_Util
from apistudy0306.apistudy.redis_study.redis_util import RedisUtil
from apistudy0306.apistudy.requests_study.mtxshop_api import buyer_login


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")


# 使用@pytest.fixture装饰的方法是一个fixture方法
# 装饰器有两个参数，一个是scope,一个是autouse
# scope表示该方法的作用域，autouse该方法是否自动调用
# scope 作用域总共有session、package、class、function、module
# session表示的是本次pytest执行中该方法只会被执行一次
# package和session几乎相同
# class 在同一个测试类中不管被调用多少次，都只执行一次
# function 每一个测试用例执行时都会被调用
# module 在同一个模块下，不管这个方法被调用多少次，都只执行一次
@pytest.fixture(scope='session', autouse=True)
def get_token():
    print('fixture里调用了登录')
    resp = buyer_login()
    uid = resp.json()['uid']
    yield uid


@pytest.fixture(scope='package', autouse=True)
def pa1():
    print('fixture里package')


@pytest.fixture(scope='class', autouse=True)
def pa2():
    print('fixture里class')


@pytest.fixture(scope='function', autouse=True)
def pa3():
    print('fixture里function')


@pytest.fixture(scope='module', autouse=True)
def pa4():
    print('fixture里module')


# 该fixture 的autouse没有写，默认是False，所以他不会被自动调用
# 因此想使用时，需要手动调用
# 调用时可以采用@pytest.mark.usefixtures('ceshilei')方式
# 也可以采用在测试用例函数中传参，参数名称就是该fixture函数名称
@pytest.fixture(scope='class')
def ceshilei():
    print('fixture里ceshilei')


@pytest.fixture(scope='class')
def qianzhi_and_houzhi():
    print('这是前置动作')
    yield  # 从这一行往后是后置动作，在这之前是前置动作
    print('这是后置动作')


@pytest.fixture(scope='class')
def return_data():
    print('这是计算数据的过程')
    yield '这是fixture的返回值'
    print('这是return_data的后置动作')


@pytest.fixture(scope='session', autouse=True)
def redis_util():
    redis_util = RedisUtil(host='121.42.15.146', pwd='testfan')
    yield redis_util


@pytest.fixture(scope='session', autouse=True)
def db_util():
    db_util = DB_Util(host='121.42.15.146', user='root', password='Testfan#123')
    yield db_util
    db_util.close()
