# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : json_util.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-09-22 21:20
# @Copyright: 北京码同学
import jsonpath
# from jsonpath_rw import  Index, Fields
# from jsonpath_rw_ext import parse

from common.logger import GetLogger


def extract_json(json_obejct,express,index=0):
    """

    :param json_obejct: 匹配的目标对象
    :param express: jsonpath表达式
    :param index: 要提取的结果中的第几个，默认是第一个，如果index小于0，则返回所有
    :return:
    """
    res = jsonpath.jsonpath(json_obejct,express)
    if res:# res如果没匹配到那么他是False，不满足条件
        # GetLogger.logger.info(f'通过{express}在{json_obejct}匹配到的结果是：{res}')
        if index<0:
            #如果index小于0，则返回所有
            return res
        else:
            #如果不小于0，那么你传几，就代表你要的是匹配结果中的某一个
            return res[index]
    else:
        # GetLogger.logger.exception(f'通过{express}在{json_obejct}没有提取到值')
        # raise Exception(f'通过{express}未匹配到值')
        return res


"""
pip install jsonpath-rw -i https://pypi.douban.com/simple
pip install jsonpath-rw-ext -i https://pypi.douban.com/simple
"""
# def update_value_to_json(json_object, json_path, new_value):
#     json_path_expr = parse(json_path)
#     # print(json_path_expr)
#     for match in json_path_expr.find(json_object):
#         # print(match)
#         path = match.path
#         print(path)
#         if isinstance(path, Index):
#             match.context.value[match.path.index] = new_value
#         elif isinstance(path, Fields):
#             match.context.value[match.path.fields[0]] = new_value
#     return json_object



if __name__ == '__main__':

    s = { "store": {
            "book": [
              { "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
              },
              { "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
              },
              { "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
              },
              { "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
              }
            ],
            "bicycle": {
              "color": "red",
              "price": 19.95,
              "author":"xxxx"
            }
          }
        }
    # 注意：jsonpath一旦能匹配到数据，不管数据有几个，返回结果都是个列表
    res = jsonpath.jsonpath(s,'$.store.bicycle.color')
    # 注意：jsonpath一旦匹配不到数据，那么结果是False
    # res = jsonpath.jsonpath(s, '$.store.bicycle.color1')
    res = jsonpath.jsonpath(s, '$.store..price')
    print(res)

    res = extract_json(s,'$.store..price',index=2)
    print(res)

    print(update_value_to_json(s, "$..author", 'shamo'))