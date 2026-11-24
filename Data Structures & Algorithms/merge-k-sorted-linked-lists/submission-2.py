# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        merge 2 linked lists and turn this into mergesort
        """
        # no lists
        if len(lists) == 0:
            return None
        # 1 list, return it
        if len(lists) == 1:
            return lists[0]
        # 2 lists, merge them
        if len(lists) == 2:
            list1 = lists[0]
            list2 = lists[1]
        # >2 lists, acquire 2 and then merge them
        if len(lists) > 2:
            list1 = self.mergeKLists(lists[:len(lists) // 2])
            list2 = self.mergeKLists(lists[len(lists) // 2:])

        # now merge them
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        while list1:
            cur.next = list1
            cur = list1
            list1 = list1.next
        while list2:
            cur.next = list2
            cur = list2
            list2 = list2.next
        return dummy.next
            

