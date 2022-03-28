# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-13 10:49
# @Copyright：北京码同学
from apiframework.api.base_api import BaseBuyerApi


class CommentApi(BaseBuyerApi):

    def __init__(self,order_sn,sku_id):
        super().__init__()
        self.url = f'{self.host}/members/comments'
        self.method = 'post'
        self.json = {
            "order_sn": order_sn,
            "delivery_score": 5,
            "description_score": 5,
            "service_score": 5,
            "comments": [{
                "sku_id": sku_id,
                "content": "这就是个评论，不要管我说啥",
                "grade": "good",
                "images": []
            }]
        }