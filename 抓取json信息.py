# -*- coding:utf-8 -*-
import os
import requests
import json

url = ('http://whattomine.com/coins/164.json')
json_dict = json.loads(requests.get(url).text)

revenue = (json_dict['revenue'])

f_revenue = float(revenue[2:])#将$符号去掉

a = f_revenue*38#计算整体收益
b = 4.61        #计算电力费用
c = a-b         #计算纯利润


print ('''本次计算使用的是2280M算力，
1600W电力损耗和1%的矿池费用。
作者：张旭
       ''')
print ('使用Lbry挖矿收益为：$',c*6.8)
print ('…………………………………')
print ('收益     费用     利润')
print ('$',(a),' $','%.2f' % (b),'  $','%.2f' % (c))#格式化数据保留2位小数点


os.system("pause") 
