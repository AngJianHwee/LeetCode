from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Convert to Doubly Link List
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p = head.next
        q = head
        while p is not None:
            print(q.val, p.val)
            p.prev = q
            q = p
            p = p.next

        p = head
        print(p.val, q.val)

        m = 0
        while p.next != q:
            m = max(m, p.val + q.val)
            p = p.next
            q = q.prev
        m = max(m, p.val + q.val)
        return m

s = Solution()


# # Only flip 2nd part
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         if head.next.next is None:
#             return head.val + head.next.val
        
#         p = head
#         # while True:
#         #     try:
#         #         print(p.val, end = " -> ")
#         #         p = p.next
#         #     except:
#         #         break
        
        
#         s = head
#         f = head.next.next
#         while f is not None:
#             s = s.next
#             f = f.next.next
        
#         s = s.next
#         p = head
#         arr = []
#         arr2 = []

#         while s is not None:
#             arr.append(p.val)
#             arr2.append(s.val)
#             s = s.next
#             p = p.next
        
#         return max([a+b for a,b in zip(arr,arr2[::-1])])
        


# # Convert to array
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         x = []
#         p = head
        
#         while p is not None:
#             x.append(p.val)
#             p = p.next
        
#         m = 0
#         for i in range(len(x)//2):
#             m = max(x[i]+x[len(x) - i - 1],m)
#         return m