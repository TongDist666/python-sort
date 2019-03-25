# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:00:05 2019

@author: TongDist
时间复杂度：N^2

最好情况下（输入数组已经有序）时间复杂度 ：N
最坏情况下（逆序）：

比冒泡和选择排序效果好
"""

list_0=input("请输入一串数字（以空格隔开）：")

list0=list_0.split()
def insert_sort(list0):
    length = len(list0)
    # 下标从1开始
    for i in range(1, length):
        if list0[i] < list0[i-1]:
            temp = list0[i]
            j = i-1
            while list0[j] > temp and j >= 0:
                list0[j+1] = list0[j]
                j -= 1
            list0[j+1] = temp
        print(list0)
insert_sort(list0)