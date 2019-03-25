# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 16:34:17 2019

@author: TongDist
优劣：

　　1. 不需要大量的辅助空间，和归并排序一样容易实现。

　　2. 希尔排序的时间复杂度与增量序列的选取有关，
      例如希尔增量时间复杂度为O(n²)，
      而Hibbard增量的希尔排序的时间复杂度为O(n^1.5)，
      希尔排序时间复杂度的下界是n*log2n。

　　3. 希尔排序没有快速排序算法快 O(n(logn))，因此中等大小规模表现良好，对规模非常大的数据排序不是最优选择。

　　4. 希尔算法在最坏的情况下和平均情况下执行效率相差不是很多，而快速排序在最坏的情况下执行的效率会非常差。
"""

def ShellInsetSort(array, len_array, dk):  # 直接插入排序
    for i in range(dk, len_array):  # 从下标为dk的数进行插入排序
        position = i
        current_val = array[position]  # 要插入的数

        index = i
        j = int(index / dk)  # index与dk的商
        index = index - j * dk

        # while True:  # 找到第一个的下标，在增量为dk中，第一个的下标index必然 0<=index<dk
        #     index = index - dk
        #     if 0<=index and index <dk:
        #         break


        # position>index,要插入的数的下标必须得大于第一个下标
        while position > index and current_val < array[position-dk]:
            array[position] = array[position-dk]  # 往后移动
            position = position-dk
        else:
            array[position] = current_val



def ShellSort(array, len_array):  # 希尔排序
    dk = int(len_array/2)  # 增量
    while(dk >= 1):
        ShellInsetSort(array, len_array, dk)
        print(">>:",array)
        dk = int(dk/2)

if __name__ == "__main__":
    list_0=input("请输入一串数字（以空格隔开）：")

    list0=list_0.split()
    print(">:", list0)
    ShellSort(list0, len(list0))