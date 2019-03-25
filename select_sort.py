# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:51:34 2019

@author: TongDist
时间复杂度：N^2

每一轮，多次比较，一次交换
比冒泡排序性能好
"""

list_0=input("请输入一串数字（以空格隔开）：")

list0=list_0.split()
def swap(a,b):
    temp=list0[a]
    list0[a]=list0[b]
    list0[b]=temp
def select_sort(list0):
    length=len(list0)
    for i in range(length):
        min_num=i
        for j in range(i+1,length):
            if list0[min_num]>list0[j]:
                min_num=j
        if i!=min_num:
            swap(i,min_num)
        print(list0)
select_sort(list0)