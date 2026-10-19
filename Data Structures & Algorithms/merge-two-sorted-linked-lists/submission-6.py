# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        new = ListNode()
        head = new
        while l1 and l2:
            if l1.val<=l2.val:
                new.next = l1
                new = new.next
                l1 = l1.next
            else:
                new.next = l2
                new = new.next
                l2 = l2.next
        new.next = l1 if l1 else l2
        return head.next

        