from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 2:
            dic = {}
            for stone in stones:
                try:
                    dic[stone] += 1
                except:
                    dic[stone] = 1
            arr1 = sorted(list(dic.items()))[::-1][0]
            arr2 = sorted(list(dic.items()))[::-1][1]
            if arr1[1] == 2:
                stones = [x for x in stones if x == arr1[0]]
                continue
            else:
                new_stones = []
                for x in stones:
                    if x == max(arr1[0], arr2[0]):
                        new_stones.append(abs(arr1[0]-arr2[0]))
                        continue
                    elif x == min(arr1[0], arr2[0]):
                        continue
                    else:
                        new_stones.append(x)
                stones = new_stones
        return stones[0]


s = Solution()
print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))


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
