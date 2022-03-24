# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-20 17:14
# @Copyright：北京码同学
import jsonpath
import requests

session = requests.session()
token = ''
def buyer_login():
    url = 'http://www.mtxshop.com:7002/passport/login'

    headers = {
        'Authorization': ''
    }
    # 查询参数通常使用params来表示
    params = {
        'username': 'shamo',
        'password': 'e10adc3949ba59abbe56e057f20f883e',
        'captcha': '1512',
        'uuid': 'jsjdhdhdhdhdhdhh'
    }
    resp = session.request(url=url,method='post', headers=headers, params=params)

    status_code = resp.status_code  # 获取响应状态码
    # print(status_code)
    # resp_info = resp.text  # 获取响应信息，返回结果是字符串格式
    resp_json = resp.json()  # 获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
    # print(resp_info)
    print(resp_json)
    global token
    # token = resp_json['access_token']
    token = jsonpath.jsonpath(resp_json,'$.access_token')[0]
    return resp
def add_cart(sku_id=5173,num=1):
    url = 'http://www.mtxshop.com:7002/trade/carts'
    global token
    headers = {
        'Authorization': token
    }
    # 查询参数通常使用params来表示
    params = {
        'sku_id': sku_id,
        'num': num
    }
    resp = session.request(url=url,method='post', headers=headers, params=params)

    # status_code = resp.status_code  # 获取响应状态码
    # # print(status_code)
    # # resp_info = resp.text  # 获取响应信息，返回结果是字符串格式
    # resp_json = resp.json()  # 获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
    # # print(resp_info)
    # print(resp_json)
    return resp
def buy_now(sku_id=5173,num=1):
    # 添加购物车接口
    url = 'http://www.mtxshop.com:7002/trade/carts/buy'
    global token
    headers = {
        'Authorization': token
    }
    # 查询参数通常使用params来表示
    params = {
        'sku_id': sku_id,
        'num': num
    }
    resp = session.request(url=url,method='post', headers=headers, params=params)

    # status_code = resp.status_code  # 获取响应状态码
    # # print(status_code)
    # # resp_info = resp.text  # 获取响应信息，返回结果是字符串格式
    # resp_json = resp.json()  # 获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
    # # print(resp_info)
    # print(resp_json)
    return resp
def set_address(address_id=3896):
    # 设置收货地址接口
    url = f'http://www.mtxshop.com:7002/trade/checkout-params/address-id/{address_id}'
    global token
    headers = {
        'Authorization': token
    }

    resp = session.request(url=url,method='post', headers=headers)

    # status_code = resp.status_code  # 获取响应状态码
    # # print(status_code)
    # # resp_info = resp.text  # 获取响应信息，返回结果是字符串格式
    # resp_json = resp.json()  # 获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
    # # print(resp_info)
    # print(resp_json)
    return resp
def set_payment_type(payment_type='COD'):
    # 设置支付类型接口
    url = 'http://www.mtxshop.com:7002/trade/checkout-params/payment-type'
    global token
    headers = {
        'Authorization': token
    }
    # 查询参数通常使用params来表示
    params = {
        'payment_type': payment_type #表示货到付款
    }
    resp = session.request(url=url,method='post', headers=headers,params=params)

    # status_code = resp.status_code  # 获取响应状态码
    # # print(status_code)
    # # resp_info = resp.text  # 获取响应信息，返回结果是字符串格式
    # resp_json = resp.json()  # 获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
    # # print(resp_info)
    # print(resp_json)
    return resp

def create_trade(client='PC',way='BUY_NOW'):
    # 创建交易接口
    url = 'http://www.mtxshop.com:7002/trade/create'
    global token
    headers = {
        'Authorization': token
    }
    # 查询参数通常使用params来表示
    params = {
        'client': client,
        'way':way
    }
    resp = session.request(url=url,method='post', headers=headers,params=params)

    # status_code = resp.status_code  # 获取响应状态码
    # # print(status_code)
    # # resp_info = resp.text  # 获取响应信息，返回结果是字符串格式
    # resp_json = resp.json()  # 获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
    # # print(resp_info)
    # print(resp_json)
    return resp
def delete_cart():
    # 设置收货地址接口
    url = 'http://www.mtxshop.com:7002/trade/carts'
    global token
    headers = {
        'Authorization': token
    }

    resp = session.request(url=url,method='delete', headers=headers)

    # status_code = resp.status_code  # 获取响应状态码
    # # print(status_code)
    # # resp_info = resp.text  # 获取响应信息，返回结果是字符串格式
    # resp_json = resp.json()  # 获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
    # # print(resp_info)
    # print(resp_json)
    return resp
if __name__ == '__main__':
    buyer_login()
    add_cart()