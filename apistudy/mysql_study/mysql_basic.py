# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 10:26
# @Copyright：北京码同学
import pymysql

connect = pymysql.Connect(
    host='121.42.15.146',
    port=3306,
    user='root',
    password='Testfan#123',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# SELECT * FROM mtxshop_trade.es_order WHERE member_id=59 ORDER BY order_id DESC LIMIT 1 ;
cursor = connect.cursor() #获取一个游标对象
# 通过游标对象去操作
cursor.execute("SELECT * FROM mtxshop_trade.es_order WHERE member_id=59 ORDER BY order_id DESC LIMIT 1 ;")
data = cursor.fetchall() #拿到执行之后的结果
cursor.close() # 关闭游标对象
connect.commit() # 提交数据
connect.close() # 关闭连接对象

print(data)
# data是一个列表，里边套着无数个字典，一个字典就是一行数据
# 拿到第一行数据
print(data[0])
# 拿到第一行数据里的trade_sn
print(data[0]['trade_sn'])