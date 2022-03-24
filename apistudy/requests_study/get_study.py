# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-20 16:24
# @Copyright：北京码同学
import requests
# 对于一个接口的调用或者说测试，都需要知道哪些东西
# 请求地址、请求headers、请求方式、请求参数、响应信息
# 卖家登录接口
url = 'http://www.mtxshop.com:7003/seller/login'

headers = {
    'Authorization':''
}
#查询参数通常使用params来表示
params = {
    'username':'shamoseller',
    'password':'e10adc3949ba59abbe56e057f20f883e',
    'captcha':'1512',
    'uuid':'jsjdhdhdhdhdhdhh'
}

# 接口的基本信息我们已经准备好了，如何发起调用
# 先导入requests库
# 发起调用并得到响应对象
# 注意这个响应包含了响应里的所有东西，我们经常关注响应状态码、响应body信息
resp = requests.get(url=url,headers=headers,params=params)

status_code = resp.status_code #获取响应状态码
print(status_code)
resp_info = resp.text #获取响应信息，返回结果是字符串格式
resp_json = resp.json()#获取响应信息，返回结果是个字典，注意这种方法只能针对响应信息是json格式
print(resp_info)
print(resp_json)