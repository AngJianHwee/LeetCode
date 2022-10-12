from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = dict({})
        for i in range(1,len(nums)+1):
            dic[i] = 1
        
        for num in nums:
            dic[num] = dic[num] - 1
        
        for x,y in dic.items():
            if y == 1:
                a = x
            if y == -1:
                b = x
                
        return a,b
                
s = Solution()
print(s.findErrorNums([1,2,2,4]))


# # Model Solution
# The idea is based on:
# (1 ^ 2 ^ 3 ^ .. ^ n) ^ (1 ^ 2 ^ 3 ^ .. ^ n) = 0
# Suppose we change 'a' to 'b', then all but 'a' and 'b' are XORed exactly 2 times. The result is then
# 0 ^ a ^ b ^ b ^ b = a ^ b
# Let c = a ^ b, if we can find 'b' which appears 2 times in the original array, 'a' can be easily calculated by a = c ^ b.