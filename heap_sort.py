# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 17:37:08 2019

@author: TongDist
空间复杂度：堆排序数据交换时需要一个辅助空间，故空间复杂度是O（1）
 
在构建堆(初始化大顶堆)的过程中，
完全二叉树从最下层最右边的非终端结点开始构建，
将它与其孩子进行比较和必要的互换，对于每个非终端结点来说，
其实最多进行两次比较和一次互换操作，
因此整个构建堆的时间复杂度为: O(n)。
大概需进行n/2 * 2 = n次比较和n/2次交换。
 
在正式排序时，n个结点的完全二叉树的深度为⌊log2n⌋+1，
并且有n个数据则需要取n-1次调整成大顶堆的操作，
每次调整成大顶堆的时间复杂度为O(log2n)。
因此，重建堆的时间复杂度可近似看做: O(nlogn)。


堆排序的运行时间主要消耗在初始构建堆和重建堆的反复筛选上。
其初始构建堆时间复杂度为O(n)。
正式排序时，重建堆的时间复杂度为O(nlogn)。
所以堆排序的总体时间复杂度为O(nlogn)。

堆排序对原始记录的排序状态不敏感，因此它无论最好、最坏和平均时间复杂度都是O(nlogn)。在性能上要好于冒泡、简单选择和直接插入算法。

空间复杂度上，只需要一个用于交换的暂存单元。但是由于记录的比较和交换是跳跃式的，因此，堆排序也是一种不稳定的排序方法。

此外，由于初始构建堆的比较次数较多，堆排序不适合序列个数较少的排序工作。
"""

def big_endian(arr, start, end):
   root = start
   while True:
       child = root * 2 + 1   # 左孩子
       if child > end:        # 孩子比最后一个节点还大 也就意味着最后一个叶子节点了 就得跳出去一次循环已经调整完毕
           break
       if child + 1 <= end and arr[child] < arr[child + 1]:   # 为了始终让其跟子元素的较大值比较 如果右边大就左换右，左边大的话就默认
           child += 1
       if arr[root] < arr[child]:     # 父节点小于子节点直接换位置 同时坐标也得换这样下次循环可以准确判断是否为最底层是不是调整完毕
           arr[root], arr[child] = arr[child], arr[root]
           root = child
       else:                            # 父子节点顺序正常 直接过
           break
            
            
def heap_sort(arr):
   # 无序区大根堆排序
   first = len(arr) // 2 - 1
   for start in range(first, -1, -1):   # 从下到上，从右到左对每个节点进调整 循环得到非叶子节点
       big_endian(arr, start, len(arr) - 1)  # 去调整所有的节点
   for end in range(len(arr) - 1, 0, -1):
       arr[0], arr[end] = arr[end], arr[0]   # 顶部尾部互换位置
       big_endian(arr, 0, end - 1)          # 重新调整子节点的顺序  从顶开始调整
   return arr
    
    
def main():
    list_0=input("请输入一串数字（以空格隔开）：")

    list0=list_0.split()
    print(heap_sort(list0))  # 原地排序
    
if __name__ == "__main__":
   main() 