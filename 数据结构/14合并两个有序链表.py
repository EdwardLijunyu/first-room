#将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        newhead = l2 if l1.val>l2.val else l1

        previors=newhead


        if newhead==l1:
            pl1 = newhead.next
            pl2 = l2

        else:
            pl1 = l1
            pl2 = newhead.next

        while pl2 and pl1:
            if pl1.val<pl2.val:
                previors.next=pl1
                previors=previors.next

                pl1=pl1.next
            else:
                previors.next = pl2
                previors = previors.next

                pl2 = pl2.next

        if pl1==None:
            previors.next=pl2

        else:
            previors.next=pl1

        return newhead



        return retnew









