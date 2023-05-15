# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-01-08 10:50
# @Copyright：北京码同学
import sys

from common.client import RequestsClient
from common.json_util import extract_json
from common.logger import GetLogger


class FeiShuNotice(RequestsClient):

    def __init__(self,url,job_name,build_number,result,user,build_url):
        super().__init__()
        self.url = url
        self.method = "post"
        self.json = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": f"{job_name} 第{build_number}次测试完成",
                        "content": [
                            [{
                                    "tag": "text",
                                    "text": f"状态：{result}"
                                }],
                                [{
                                    "tag": "text",
                                    "text": f"执行人: {user}"
                                }],
                                [{
                                    "tag": "a",
                                    "text": "查看报告",
                                    "href": f"{build_url}/allure"
                                }]

                        ]
                    }
                }
            }
        }
class JenkinsStutus(RequestsClient):
    def __init__(self,build_url,username,password):
        # http://localhost:8080/job/feishu/1/api/json
        super().__init__()
        self.url = f'{build_url}/api/json'
        self.method = 'get'
        self.session.auth = (username,password)

if __name__ == '__main__':
    GetLogger.get_logger("feishu")  # 初始化logger对象
    agrs = sys.argv
    print(agrs)
    build_url = agrs[1]
    username = agrs[2]
    password = agrs[3]
    fishu_url = agrs[4]
    job_name = agrs[5]
    build_number = agrs[6]
    # 调用任务执行数据
    jenkins_result = JenkinsStutus(build_url,username,password)
    res = jenkins_result.send()
    print(res)
    # 获取任务执行人
    # # user = jenkins_result.extract_resp("$..userName")
    user = extract_json(res.json(),'$..userName')
    ## 获取任务执行结果
    # result = jenkins_result.extract_resp("$..result")
    result = extract_json(res.json(),'$..result')
    # https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=783da784-95dd-41c5-ae51-31a2d89c3ce9
    FeiShuNotice(fishu_url,job_name,build_number,result,user,build_url).send()