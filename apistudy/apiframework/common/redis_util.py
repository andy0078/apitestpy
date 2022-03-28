# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-27 16:35
# @Copyright：北京码同学
import javaobj
import redis


class RedisUtil:
    # decode_responses设置为true以字符串形式得到数据，设置为False以二进制形式得到
    def __init__(self,host,pwd,port=6379,decode_responses=False):
        self.pool = redis.ConnectionPool(host=host,password=pwd, port=port, decode_responses=decode_responses,encoding_errors='ignore')
        self.r = redis.Redis(connection_pool=self.pool)  # 表示从上面的连接池拿到一个连接对象
    def get(self,key):
        type = self.r.type(key).decode('utf8')
        if type == 'string':
            return self.r.get(key)
        elif type == 'hash':
            return  self.r.hgetall(key)
        elif type == 'zset':
            return self.r.zrange(key,0,-1)
        elif type == 'set':
            return self.r.smembers(key)
        elif type == 'list':
            return self.r.lrange(key,0,-1)
        else:
            raise Exception(f'不支持的数据类型{type}或者{key}不存在')
if __name__ == '__main__':
    redis_util = RedisUtil(host='121.42.15.146',pwd='testfan')
    # 立即购买接口的缓存数据
    # res = redis_util.get('{BUY_NOW_ORIGIN_DATA_PREFIX}_59') # 这个key后面的数字是根据用户发生变化，是用户id
    # print(res)
    # # 商城项目后台开发语言是java，存redis数据时，存的是java对象
    # # 立即购买的对象是一个List集合，里边放的是CartSkuOriginVo对象，这些都是java里的
    # # 无法直接解析，因此要使用一个第三方库，javaobj-py3，这个库可以帮我们将java类型的序列化数据转换成python对象
    # res_list = javaobj.loads(res) # 这是得到结果转换成python的列表
    # print(res_list)
    # # 业务上这个列表中，只会存储一个数据
    # obj = res_list[0] #通过索引得到列表里的数据
    # # 立即购买存储的实际上是产品订单的一些信息，这个对象必然具备非常多的属性
    # print(dir(obj)) # 可以使用这个方法来看obj对象都有哪些属性，但最佳的方式还是直接问比较好
    # # print(obj.__getattribute__('price'))
    # print(obj.__getattribute__('num'))
    # print(obj.__getattribute__('skuId'))

    # 订单设置相关参数的缓存数据
    res = redis_util.get('{CHECKOUT_PARAM_ID_PREFIX}_59')
    print(res)
    print(type(res))
    # res是个字典
    for key,value in res.items():
        key = javaobj.loads(key)
        # print(key)
        try:
            value = javaobj.loads(value)
            if key == 'addressId':
                print(value)
            if key== 'paymentType':
                value = value.__getattribute__('constant')
                # print(dir(value))
        except:
            pass
        print(f'{key}:{value}')

