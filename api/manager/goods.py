# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-13 11:39
# @Copyright：北京码同学
from  api.base_api import BaseManagerApi


class AuditGoodsApi(BaseManagerApi):

    # 注意该参数goods_id要求是一个列表
    def __init__(self,goods_ids:list):
        super().__init__()
        self.url = f'{self.host}/admin/goods/batch/audit'
        self.method = 'post'
        self.json = {
            "goods_ids": goods_ids,
            "message": "aaaa",
            "pass": 1
        }