from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0
        upper = x+1
        lower = 1
        while (upper - lower)>1e-5:
            # print(lower, upper)
            middle = lower + (upper - lower)/2
            if middle**2 > x:
                upper = middle
            else:
                lower = middle
        return int(upper)



s = Solution()
print(s.mySqrt(9))
print(s.mySqrt(10))
print(s.mySqrt(2147395599))



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
