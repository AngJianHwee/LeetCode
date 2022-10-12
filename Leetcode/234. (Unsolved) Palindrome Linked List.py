from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = slow.next
        while fast is not None:
            slow = slow.next
            fast = fast.next.next
        
        

                
s = Solution()


# # Model Solution
# The idea is based on:
# (1 ^ 2 ^ 3 ^ .. ^ n) ^ (1 ^ 2 ^ 3 ^ .. ^ n) = 0
# Suppose we change 'a' to 'b', then all but 'a' and 'b' are XORed exactly 2 times. The result is then
# 0 ^ a ^ b ^ b ^ b = a ^ b
# Let c = a ^ b, if we can find 'b' which appears 2 times in the original array, 'a' can be easily calculated by a = c ^ b.


# import time
# for i in range(5):
#     print(i,end = "\r")
#     time.sleep(1)