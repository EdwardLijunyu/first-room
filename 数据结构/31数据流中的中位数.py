


'''

如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。


'''
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A=[]#存放大于中位数的一半
        self.B=[]#存放小于中位数的一半


    def addNum(self, num: int) -> None:
        if len(self.A)==len(self.B):         #heappop弹出的是堆的最小值，堆的根节点
            heapq.heappush(self.B,-num)
            heapq.heappush(self.A,-heapq.heappop(self.B))#将B中最大值给A
        else:
            heapq.heappush(self.A,num)
            heapq.heappush(self.B,-heapq.heappop(self.A))#将A中最小值给B


    def findMedian(self) -> float:
        if len(self.A)==len(self.B):
            return (self.A[0]-self.B[0])/2.0 #A中的最小值和B中的最大值就是中间位置
        else:
            return self.A[0]  #A[0]小于A中后面的数，大于B中的数，所以是中位数
