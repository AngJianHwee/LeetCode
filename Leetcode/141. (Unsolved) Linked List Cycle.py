from typing import List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        visited = [id(p)]
        while p.next is not None:
            p = head.next
            if id(p) in visited:
                return False
            visited.append(id(p))
        return True

        


s = Solution()
print(s.areAlmostEqual(s1="bank", s2="kanb"))
print(s.areAlmostEqual(s1="attack", s2="defend"))
print(s.areAlmostEqual(s1="kelb", s2="kelb"))
print(s.areAlmostEqual(s1="a", s2="b"))
print(s.areAlmostEqual(s1="ab", s2="ba"))
print(s.areAlmostEqual("npv","zpn"))
print(s.areAlmostEqual("abca","abcc"))

