# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 20:05
# @Author  : SDYL
# @Email   : sdyl_1020@163.com
# @File    : getTargeting.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 18:14
# @Author  : SDYL
# @Email   : sdyl_1020@163.com
# @File    : antColonyAlgorithm.py
# @Software: PyCharm


import requests
from bs4 import BeautifulSoup
import csv
import re
import time
import json


def getlocation(name):                          # 调用百度API查询地理位置
    bdurl = "http://api.map.baidu.com/geocoding/v3/?address="
    output = 'json'
    ak = 'BS8vngLVtU6oABLfGOdEfUUM34NTm8rY'
    callback = 'showLocation'
    uri = bdurl + name + '&output=' + output + '&ak=' + ak + '&callback=' + callback + '&city=武汉'

    print(uri)
    res = requests.get(uri)

    s = BeautifulSoup(res.text, features="lxml")
    # print(s.prettify())

    # print(type(s))
    s = str(s.find_all('p'))
    # print(s)
    js_s = re.findall(re.compile(r"[(](.*?)[)]"), s)
    js_s = str(js_s[0])
    # print(json)
    locDict = json.loads(js_s)
    if locDict['status'] == 1:
        return
    # print(locDict)
    result = locDict['result']
    # print(result)
    if not result:
        return None
    else:
        location = result['location']

        loc_S = str(location['lng']) + ',' + str(location['lat'])
        return loc_S


with open('name.txt', 'r', encoding='utf-8') as f:
    projectNameList = f.readlines()

print(projectNameList)

n = 0
num = len(projectNameList)

file = open('cgdw.csv', 'w', newline='')
headers = ['name', 'loc']
writers = csv.DictWriter(file, headers)
writers.writeheader()
while n < num:      # 循环放入消息列表
    h0 = projectNameList[n].split(r'\\t\\n')
    print(h0)
    name = h0[0]
    loc = getlocation(name)
    print(loc)
    # 将定位信息写入dict
    house = {'name': name, 'loc': loc}
    try:
        writers.writerow(house)         # dict to csv

    except Exception as e:
        print(e)
        # continue
    n += 1
    print(n)
file.close()
