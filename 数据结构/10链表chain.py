class ListNode:
    def __init__(self,x):
        self.value=x
        self.next=None

if __name__=='__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)

    l1.next = l2
    l2.next = l3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#从尾到头打印链表，用数组储存反向链表元素
class Solution:
    def reversePrint(self, head: ListNode) :
        ret=[]
        while head:           #这一句记住，循环所有链表元素
            ret.insert(0,head.value)
            head=head.next
        return ret


example=Solution()
print(example.reversePrint(l1))

