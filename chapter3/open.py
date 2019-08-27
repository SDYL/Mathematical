# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 1:37
# @Author  : SDYL
# @Email   : sdyl_1020@163.com
# @File    : open.py
# @Software: PyCharm

import csv
import pandas as pd                         #导入pandas包
# def func01():
#     with open('lz.csv', 'r', newline='') as csvfile:
#
#         writer = csv.writer(csvfile)
#         print(type(writer))
#         # for item in writer:
#         # print(item)
#
# func01()


data = pd.read_csv("lz.csv", 'utf-8', engine='python')             #读取csv文件
# print(data)                                #打印所有文件pr
# print(data.head(50))                        #打印前5行
# print(data.columns)                         #返回全部列名
# print(data.shape)                           #f返回csv文件形状
# print(data.loc[1:2])                        #打印第1到2行
# data.loc[2:4, ['PassengerId', 'Sex']]       #打印行中特定列
print(data[:, ['空气质量级别']]













































































      )

# csvFile = open("csvData.csv", "w")            #创建csv文件
# writer = csv.writer(csvFile)                  #创建写的对象
# #先写入columns_name
# writer.writerow(["index","a_name","b_name"])     #写入列的名称
# #写入多行用writerows                                #写入多行
# writer.writerows([[1,a,b],[2,c,d],[3,d,e]])
# csvFile.close()