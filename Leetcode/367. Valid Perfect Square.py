from typing import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lower = 0
        upper = num + 1
        while (upper - lower) > 1:
            middle = lower + (upper - lower)//2
            if middle**2 >= num:
                upper = middle
            else:
                lower = middle
        return upper**2 == num


s = Solution()
print(s.isPerfectSquare(4))
print(s.isPerfectSquare(999))
print(s.isPerfectSquare(1024))

