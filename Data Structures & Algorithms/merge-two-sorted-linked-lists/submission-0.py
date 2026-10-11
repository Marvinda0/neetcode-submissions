# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode(0,)
        head = new
        l1, l2 = list1, list2
        while l1 is not None and l2 is not None:
            if l1.val<=l2.val:
                new.next = l1
                new = l1
                l1 = l1.next
            else:
                new.next = l2
                new = l2
                l2 = l2.next
        if l1 is None:
            new.next = l2
        else:
            new.next = l1
        return head.next
                
        
                
                 
        

        