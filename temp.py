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
