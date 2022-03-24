# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-27 16:15
# @Copyright：北京码同学

import redis
# host指的就是redis服务的ip地址，port指的是redis服务的端口
pool = redis.ConnectionPool(host='127.0.0.1',port=6379,decode_responses=True)
r = redis.Redis(connection_pool=pool) #从redis连接池中得到一个redis操作对象

# 针对字符串的操作
# key是"gender" value是"male" 将键值对存入redis缓存,有效期300秒
r.set('gender', 'male',ex=300) # key是"name" value是"shamo"
# 将键值对存入redis缓存,有效期30000毫秒
r.set('name', 'shamo',px=30000)
# 取出键gender对应的值
print(r.get('gender'))
#批量获取，取出键gender、name对应的值
print(r.mget('gender', 'name'))

# 操作哈希值
r.hset('user1','name','shamo')
r.hset('user1','age',18)
r.hset('user1','job','tester')
print(r.hgetall('user1'))
# print(r.hmget('user2'))

# 操作列表
r.lpush('list1','data1','data2')
print(r.lrange('list1',0,-1))

# 操作集合
r.sadd('set1','data1','data2')
print(r.smembers('set1'))

# 操作有序集合
r.zadd('zset2',{'data1':1,'data2':2})
print(r.zrange('zset2',0,-1))

print(r.type('zset2')) #获取某个key对应的数据类型