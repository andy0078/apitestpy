# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-03-06 13:32
# @Copyright：北京码同学
import jsonpath

s = {"trade_sn":"20220306000052","member_id":59,"member_name":"shamo","payment_type":"COD","price_detail":{"total_price":179.0,"original_price":179.0,"goods_price":179.0,"freight_price":0.0,"discount_price":0.0,"cash_back":0.0,"coupon_price":0.0,"full_minus":0.0,"is_free_freight":0,"exchange_point":0},"consignee":{"consignee_id":3716,"name":"金枝","province":"北京","city":"朝阳区","county":"三环以内","town":None,"address":"北京","mobile":"18888888888","telephone":None,"province_id":1,"county_id":2799,"city_id":72,"town_id":0},"coupon_list":None,"order_list":[{"seller_id":20,"shipping_type_id":None,"shipping_type_name":None,"seller_name":"沙陌的店","weight":2.0,"price":{"total_price":179.0,"original_price":179.0,"goods_price":179.0,"freight_price":0.0,"discount_price":0.0,"cash_back":0.0,"coupon_price":0.0,"full_minus":0.0,"is_free_freight":0,"exchange_point":0},"sku_list":[{"seller_id":20,"seller_name":"沙陌的店","goods_id":4942,"sku_id":5173,"sku_sn":"shamo001","cat_id":83,"num":1,"purchase_num":0,"goods_weight":2.0,"original_price":179.0,"purchase_price":179.0,"subtotal":179.0,"name":"沙陌**炒锅","goods_image":"http://www.mtxshop.com:7000/statics/attachment/goods/2021/12/13/21/50442449.png_300x300.png","template_script":None,"checked":1,"is_free_freight":1,"single_list":[],"group_list":[],"promotion_tags":[],"not_join_promotion":0,"template_id":0,"spec_list":None,"point":None,"snapshot_id":None,"service_status":"NOT_APPLY","last_modify":1640517899,"enable_quantity":9998714,"rule":None,"invalid":0,"error_message":"","is_ship":1,"goods_type":"NORMAL"}],"gift_list":[],"gift_coupon_list":[],"gift_point":None,"invalid":None,"trade_sn":"20220306000052","sn":"20220306000052","consignee":{"consignee_id":3716,"name":"金枝","province":"北京","city":"朝阳区","county":"三环以内","town":None,"address":"北京","mobile":"18888888888","telephone":None,"province_id":1,"county_id":2799,"city_id":72,"town_id":0},"shipping_id":0,"payment_type":"COD","ship_time":None,"receive_time":"任意时间","member_id":59,"member_name":"shamo","remark":"","create_time":1646538406,"shipping_type":None,"order_status":"NEW","pay_status":"PAY_NO","ship_status":"SHIP_NO","ship_name":None,"order_price":179.0,"shipping_price":None,"comment_status":"UNFINISHED","disabled":None,"payment_method_id":None,"payment_plugin_id":None,"payment_method_name":None,"payment_account":None,"goods_num":1,"warehouse_id":None,"cancel_reason":None,"ship_province_id":None,"ship_city_id":None,"ship_region_id":None,"ship_town_id":None,"ship_province":None,"ship_city":None,"ship_region":None,"ship_town":None,"signing_time":None,"the_sign":None,"admin_remark":None,"address_id":None,"need_pay_money":179.0,"ship_no":None,"logi_id":None,"logi_name":None,"need_receipt":0,"receipt_title":None,"receipt_content":None,"service_status":"NOT_APPLY","client_type":"PC","receipt_history":None,"order_type":"NORMAL","order_data":None,"goods_coupon_prices":None}],"gift_list":None}

# 从其中提取trade_sn
# 当找不到结果时，返回的是False
# 如果有结果，不管是1个还是多个，那么返回的数据类型是列表
res = jsonpath.jsonpath(s,'$.trade_sn')
print(res[0])
# 提取sn，sn的路径比较深
res = jsonpath.jsonpath(s,'$..sn')
print(res[0])

# 获取total_price
res = jsonpath.jsonpath(s,'$.price_detail.total_price')
print(res[0])



