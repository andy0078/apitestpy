# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-27 9:53
# @Copyright：北京码同学
from apistudy0306.apistudy.requests_study.mtxshop_api import *

# 当前模块下所有的测试用例在调用接口之前，都先调用了登录接口
# 因此我们可以使用pytest的模块级别的前置动作来完成登录的接口调用

# 模块级别的前置
def setup_module():
    buyer_login()
    print('这是在当前模块所有测试用例执行之前，只执行一次的前置动作')

# 比如当前模块下所有用例执行完成后，要清除相关的测试数据，那么可以使用后置
def teardown_module():
    print('当前模块下，所有用例执行完后，我来做后置动作')

# 函数级别的前置和后置
def setup_function():
    buyer_login()
    print('每条测试用例执行前，我都会执行')
def teardown_function():
    buyer_login()
    print('每条测试用例执行后，我都会执行')

def test_add_cart():
    # 测试添加购物车接口
    # 先调用登录接口，否则会没有权限
    # buyer_login()
    # 调用接口，得到响应对象
    resp = add_cart()
    # 拿到resp对象以后，根据期望结果的需求进行判断
    # 预期响应状态码为200
    status_code = resp.status_code
    assert status_code == 200

# 在之前的封装中，每个接口的参数都是写死的，无法针对各个参数的测试用例传递数据
# 因此我们需要修改原来的接口定义中的参数传递

# 测试添加购物车sku_id不存在
def test_add_cart1():
    # 测试添加购物车接口
    # 先调用登录接口，否则会没有权限
    # buyer_login()
    # 调用接口，得到响应对象
    resp = add_cart(sku_id=6354535)
    # 拿到resp对象以后，根据期望结果的需求进行判断
    # 预期响应状态码为500
    status_code = resp.status_code
    print(resp.json())
    assert status_code == 500
    # 如果还想针对响应信息中的某些字段做校验，就需要进一步操作
    # {'code': '451', 'message': '商品已失效，请刷新购物车'}
    # 判断响应中的业务码是451
    resp_json = resp.json() #获取响应结果,数据类型是字典
    code = resp_json['code']
    assert code == '451'
    # 判断message的值是 商品已失效，请刷新购物车
    message = resp_json['message']
    assert message == '商品已失效，请刷新购物车'
# 测试添加购物车num为0
def test_add_cart2():
    # 测试添加购物车接口
    # 先调用登录接口，否则会没有权限
    # buyer_login()
    # 调用接口，得到响应对象
    resp = add_cart(num=0)
    # 拿到resp对象以后，根据期望结果的需求进行判断
    # 预期响应状态码为400
    status_code = resp.status_code
    print(resp.json())
    assert status_code == 400
    # 如果还想针对响应信息中的某些字段做校验，就需要进一步操作
    # {'code': '004', 'message': '加入购物车数量必须大于0'}
    # 判断响应中的业务码是004
    resp_json = resp.json() #获取响应结果,数据类型是字典
    code = resp_json['code']
    assert code == '004'
    # 判断message的值是 商品已失效，请刷新购物车
    message = resp_json['message']
    assert message == '加入购物车数量必须大于0'

