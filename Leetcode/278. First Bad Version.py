from typing import List

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower = 0
        upper = n + 1
        while (upper - lower) > 1:
            middle = lower + (upper - lower)//2
            if isBadVersion(middle):
                upper = middle
            else:
                lower = middle
        return upper

s = Solution()

