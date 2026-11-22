# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = []
        temp = head
        if head.next == None:
            return None
        if head.next.next == None:
            if n == 1:
                head.next = None
                return head
            if n == 2:
                return head.next
        while temp:
            l.append(temp)
            temp = temp.next
        if n == len(l):
            return l[1]
        if n == 1:
            l[-2].next = None
        else:
            l[-n-1].next = l[-n+1]
        return head
