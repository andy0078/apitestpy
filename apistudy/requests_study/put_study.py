# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-20 16:48
# @Copyright：北京码同学



import requests

url = 'http://82.156.74.26:9088/pinter/com/phone'
# json格式的参数通常以json来表示
json = {"brand":"Huawei","color":"yellow","memorySize":"64G","cpuCore":"8核","price":"8848","desc":"全新上市"}

resp = requests.delete(url=url,json=json)
status_code = resp.status_code #获取响应状态码
print(status_code)
resp_info = resp.text #获取响应信息，返回结果是字符串格式
resp_json = resp.json()#获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
print(resp_info)
print(resp_json)