# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。


'''

思路:
1.先确定链表是否含有环，通过快慢两个指针一次移动，如果没有快指针能追上慢指针就说明有环
2.确定有环之后，当快慢指针重合的时候，再让一个指针成从头指针开始，两个同时移动，直到两个指针重合时就是环的入口节点

'''


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        #先判断是否有环
        slow_node=pHead
        fast_node = pHead

        while fast_node.next!=None and fast_node.next.next!=None:
            fast_node=fast_node.next.next
            slow_node=slow_node.next

            if fast_node==slow_node:
                break

        if fast_node.next==None or fast_node.next.next==None:
            return None  #无环返回None

        # 执行2
        if fast_node==slow_node:
            slow_node=pHead
            while fast_node!=slow_node:
                fast_node=fast_node.next
                slow_node=slow_node.next

            return slow_node

#提交成功



















