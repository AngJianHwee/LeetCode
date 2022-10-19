# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         p = head
#         while p is not None:
#             if p.val == 0:
#                 q = p.next
#                 s = 0
#                 while q is not None and q.val != 0:
#                     s += q.val
#                     q = q.next
#                 p.val = s
#                 p.next = q
#             if p.next.next is None:
#                 p.next = None
#             p = p.next
            
            
#         return head


# Better
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head.next
        
        if p1 is None:
            return head
        
        s = 0
        while p2.next is not None:
            if p2.val != 0:
                s += p2.val
            else:
                p1.val = s
                p1 = p1.next
                s = 0
            p2 = p2.next
        p1.val = s
        p1.next = None
        return head