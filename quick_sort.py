# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 17:15:31 2019

@author: TongDist
对于绝大多数输入数据达到O(nlogn)的期望时间复杂度
这样在数组已经有序的情况下，每次划分将得到最坏的结果。O(n^2)

最好情况
　　如果每次划分过程产生的区间大小都为n/2，则快速排序法运行就快得多了。这时有：

 
　　T(n)=2T(n/2)+θ(n),T(1)=θ(1) (3)

 
　　解得：T(n)=θ(nlogn)
  
最坏情况
最坏情况发生在每次划分过程产生的两个区间分别包含n-1个元素和1个元素的时候。
时间复杂度为o（n^2）。
"""
list_0=input("请输入一串数字（以空格隔开）：")

list0=list_0.split()
#quick sort

def quickSort(array):
    if len(array) < 2:  # 基线条件（停止递归的条件）
        return array
    else:  # 递归条件
        baseValue = array[0]  # 选择基准值
        less, equal, greater = [], [baseValue], []
        for m in array[1:]:    
            if m < baseValue:        
                # 由所有小于基准值的元素组成的子数组
                less.append(m)         
            elif m > baseValue:        
                # 由所有大于基准值的元素组成的子数组
                greater.append(m)    
            else:        
                # 包括基准在内的同时和基准相等的元素，在上一个版本的百科当中，并没有考虑相等元素
                equal.append(m)
        return quickSort(less) + equal + quickSort(greater)
    
# 示例：
print(quickSort(list0))