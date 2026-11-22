# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        head = prev
        while list1 is not None or list2 is not None:
            new = ListNode()
            if list2 is None or (list1 is not None and list1.val < list2.val):
                new.val = list1.val
                list1 = list1.next
            else:
                new.val = list2.val
                list2 = list2.next
            
            prev.next = new
            prev = new
        return head.next