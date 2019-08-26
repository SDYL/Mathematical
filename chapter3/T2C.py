# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 0:55
# @Author  : SDYL
# @Email   : sdyl_1020@163.com
# @File    : T2C.py
# @Software: PyCharm
import csv

# attention! 设置newline，否则会出现两行之间有一行空行
with open('lz.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    data = open('lz.txt')  # 改成自己的路径
    for each_line in data:
        a = each_line.split()  # 我的数据每行都是字符串，所以将str按空格分割，变成list
        if a[4] == 'Ⅰ':
            a[4] = 1
        elif a[4] == 'Ⅱ':
            a[4] = 2
        elif a[4] == 'Ⅲ1':
            a[4] = 3.1
        elif a[4] == 'Ⅲ2':
            a[4] = 3.2
        elif a[4] == 'Ⅲ3':
            a[4] = 3.3
        elif a[4] == 'Ⅳ1':
            a[4] = 4.1
        elif a[4] == 'Ⅳ2':
            a[4] = 4.2
        elif a[4] == 'Ⅴ':
            a[4] = 5

        print(a[4])
        writer.writerow(a)
# 这时转换成csv文件的数据就有了！！
