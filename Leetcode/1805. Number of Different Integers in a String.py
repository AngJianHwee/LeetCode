from typing import List


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = "".join([word_ if word_.isdigit() else " " for word_ in word])
        word = [int(x) for x in word.split(" ") if x != ""]
        return len(set(word))

s = Solution()
print(s.numDifferentIntegers("a123bc34d8ef34"))
print(s.numDifferentIntegers("leet1234code234"))
print(s.numDifferentIntegers("a1b01c001"))


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
