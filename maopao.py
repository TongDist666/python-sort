# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:01:15 2019

@author: TongDist
时间复杂度：N^2
"""
import time
list=input("请输入一串数字（以空格隔开）：")

list_0=list.split()
print(list_0)
def swap(a,b):
    temp=list_0[a]
    list_0[a]=list_0[b]
    list_0[b]=temp
length=len(list_0)
#n个输入，需要n-1个pop
def pop_sort(list_0):
    for i in range(0,length-1):
        j=length-2
        while j>=i:
            if list_0[j]>list_0[j+1]:
                swap(j,j+1)
                #print(j)
            j-=1
        print("num "+str(i+1)+" pop:")
        print(list_0)
#如果一次pop没改变，认为已经排好序列
def pop_sort_advance(list_0):
    flag=True
    i=0
    while i<length-1 and flag:
        flag=False
        j=length-2
        while j>=i:
            if list_0[j]>list_0[j+1]:
                swap(j,j+1)
                flag=True
                #print(j)
            j-=1
        i+=1
        print("num "+str(i)+" pop:")
        print(list_0)
start = time.time()
pop_sort(list_0)
#pop_sort_advance(list_0)
end = time.time()
print("持续时间："+str(end-start))
print(list_0)