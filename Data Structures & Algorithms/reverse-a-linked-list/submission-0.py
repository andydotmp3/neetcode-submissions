# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curChain = ListNode(val=head.val)
        current = head.next
        while current is not None:
            newNode = ListNode(val=current.val, next=curChain)
            curChain = newNode
            current = current.next
        return curChain

