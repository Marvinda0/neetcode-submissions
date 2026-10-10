# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        if not head:
            return head
        temp = head.next
        head.next = None
        while temp:
            temp2 = temp.next
            temp.next = head
            head = temp
            temp = temp2
        return head
        