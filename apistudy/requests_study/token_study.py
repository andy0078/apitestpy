# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-20 17:09
# @Copyright：北京码同学


import requests
#这个session对象可以帮我们自动的关联cookie
#只要多个接口使用的是同一个session对象发起的接口调用，那么会自动关联cookie
# 但是他不会帮我们自动关联token，token需要自行处理
session = requests.session() #这个session对象可以帮我们自动的关联cookie

# 先完成登录接口
url = 'http://82.156.74.26:9088/pinter/bank/api/login2'

data = {
    "userName":"shamo",
    "password":"1253554"
}
resp = session.request(url=url,method='post',data=data)
status_code = resp.status_code #获取响应状态码
print(status_code)
resp_info = resp.text #获取响应信息，返回结果是字符串格式
resp_json = resp.json()#获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
print(resp_info)
print(resp_json) # {'code': '0', 'message': 'success', 'data': '90e6488e44704f789936a36c8b2e5acf'}
# 从响应信息中提取data字段作为token
# resp.json()得到的是响应结果的字典形式，那么从字典中获取某个key对应的值
token = resp_json['data']

# 调用查询余额的接口
url = 'http://82.156.74.26:9088/pinter/bank/api/query2'

headers = {
    "testfan-token":token
}

params = {
    "userName":"shamo"
}
resp = session.request(url=url,method='get',headers=headers,params=params)
status_code = resp.status_code #获取响应状态码
print(status_code)
resp_info = resp.text #获取响应信息，返回结果是字符串格式
resp_json = resp.json()#获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
print(resp_info)
print(resp_json)