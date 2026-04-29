# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i,j = list1, list2
        head = res_head = ListNode()
        while i and j :
            if i.val <= j.val:
                res_head.next = i
                i = i.next
            else:
                res_head.next = j
                j = j.next

            res_head = res_head.next
        
        res_head.next = i or j  

        return head.next