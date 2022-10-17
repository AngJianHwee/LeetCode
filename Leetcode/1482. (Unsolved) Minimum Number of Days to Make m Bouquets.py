from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        req = m*k
        if len(bloomDay) < req:
            return -1
        elif len(bloomDay) == req:
            return max(bloomDay)
        else:
            return sorted(bloomDay)[:req][-1]

s = Solution()
print(s.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2))
print(s.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))
print(s.minDays([7,7,7,7,12,7,7], m = 2, k = 3))