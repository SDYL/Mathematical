# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 11:00
# @Author  : SDYL
# @Email   : sdyl_1020@163.com
# @File    : main.py
# @Software: PyCharm

import numpy as np
import openpyxl
import matplotlib as mpl
import matplotlib.pyplot as plt


def getXlsx():
    # 获取 工作簿对象
    workbook = openpyxl.load_workbook("Project - venue.xlsx")  # 文件路径
    # 获取工作簿 workbook的所有工作表
    shenames = workbook.sheetnames
    # 获得工作簿的表名后，就可以获得表对象
    # 获取Sheet1表对象
    worksheet_Project = workbook[shenames[0]]
    # 获取Sheet2表对象
    worksheet_Venue = workbook[shenames[1]]
    tableName0 = worksheet_Project.title
    tableName1 = worksheet_Venue.title
    print(tableName0)
    print(tableName1)
    # 获取该表相应的行数和列数
    rows0 = worksheet_Project.max_row
    columns0 = worksheet_Project.max_column
    # 获取该表相应的行数和列数
    print(rows0, columns0)
    rows = worksheet_Venue.max_row
    columns = worksheet_Venue.max_column
    print(rows, columns)
    # 输出特定的列
    list00 = []
    for cell in list(worksheet_Project.columns)[0]:  # 获取第1列的数据
        list00.append(cell.value)
    print(list00)
    # 输出特定的列
    list01 = []
    for cell in list(worksheet_Venue.columns)[1]:  # 获取第1列的数据
        list01.append(cell.value)
    print(list01)
    # newList = []
    # for i in list01:
    #     if i not in newList:
    #         newList.append(i)



# 输入喜爱项目 形成偏好向量
def setProject():
    pass
# 将项目对应的场馆写入矩阵
# 拟定27个项目分布在35个场馆内 27*35 矩阵表示 项目对应的场馆
# 第一行开始依次表示为 羽毛球、乒乓球、。。。跳伞。跳水
# 第一列表示各个场馆分别为 武汉全民健身中心

def venueProject():
    N = np.zeros((27, 35))
    print(N)

    # for item in N:
    #     pass

# 通过偏好向量映射对应场馆
def calculate():
    pass

# def main():
#     # 获取xlsx指定内容
#     nameList, numList = getXlsx()
#     print(nameList)
#     print(type(nameList[0]))
#     print(numList)
#
#     # # 画图
#     # x = range(len(numList))
#     # y = numList
#     # tick_label = nameList
#     # M = plt.barh(x, y, align="center", color="c",
#     #              tick_label=tick_label,
#     #              hatch="")
#     # autolabel(M)
#     #
#     # plt.show()


# venueProject()
getXlsx()