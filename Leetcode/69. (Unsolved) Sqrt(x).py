from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 4:
            return 1
        if 4<=x<9:
            return 2
        upper = x
        lower = 1
        while (upper - lower)>0.5:
            if upper**2 <x:
                break
            if lower**2 >x:
                break
            
            middle = (upper + lower)/2
            if (middle**2)<x:
                lower = middle
            else:
                upper = middle
        return int(upper)


s = Solution()
# print(s.mySqrt(4))
print(s.mySqrt(9))
print(s.mySqrt(10))
print(s.mySqrt(16))
print(s.mySqrt(81))
print(s.mySqrt(100))
print(s.mySqrt(2147395599), 2147395599**(0.5))


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


