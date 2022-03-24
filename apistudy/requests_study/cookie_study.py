# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-20 17:02
# @Copyright：北京码同学

import requests

#这个session对象可以帮我们自动的关联cookie
#只要多个接口使用的是同一个session对象发起的接口调用，那么会自动关联cookie
session = requests.session() #这个session对象可以帮我们自动的关联cookie

# 先完成登录接口
url = 'http://82.156.74.26:9088/pinter/bank/api/login'

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
print(resp_json)

# 调用查询余额的接口
url = 'http://82.156.74.26:9088/pinter/bank/api/query'

params = {
    "userName":"shamo"
}
resp = session.request(url=url,method='get',params=params)
status_code = resp.status_code #获取响应状态码
print(status_code)
resp_info = resp.text #获取响应信息，返回结果是字符串格式
resp_json = resp.json()#获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
print(resp_info)
print(resp_json)