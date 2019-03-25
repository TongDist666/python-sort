# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 16:59:34 2019

@author: TongDist
先取一个小于n的整数d1作为第一个增量，
    把文件的全部记录分组。
    所有距离为d1的倍数的记录放在同一个组中。
    先在各组内进行直接插入排序；
然后，取第二个增量d2<d1重复上述的分组和排序，
    直至所取的增量  =1(  <  …<d2<d1)，即所有记录放在同一组中进行直接插入排序为止。
"""
list_0=input("请输入一串数字（以空格隔开）：")

list0=list_0.split()
def shell(arr):
    n=len(arr)
    h=1
    while h<n/3:
        h=3*h+1
        print(h)
    while h>=1:
        for i in range(h,n):
            j=i
            while j>=h and arr[j]<arr[j-h]:
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j-=h
            print(arr)
        h=h//3
        print(arr)
shell(list0)