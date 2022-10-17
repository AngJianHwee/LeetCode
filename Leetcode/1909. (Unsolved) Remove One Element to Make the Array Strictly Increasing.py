from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count = 0
        at = []
        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i]:
                count += 1
                at.append(i)
        if count == 0:
            return True
        elif count > 1:
            return False
        else:
            at = at[0]
            if at == 0:
                return True
            if at == len(nums) -1:
                return True
            else:
                return bool(max(nums[at-1] < nums[at+1], nums[at] < nums[at+2]))



import numpy as np
s = Solution()
print(s.canBeIncreasing(nums = [1,2,10,5,7]))
print(s.canBeIncreasing(nums = [2,3,1,2]))
print(s.canBeIncreasing(nums = [1,1,1]))
print(s.canBeIncreasing(nums = [100,21,100]))
print(s.canBeIncreasing(nums = [105,924,32,968]))

# x = list(np.random.randint(20, size=(1, 10)))[0]
# print("[" + ",".join([str(x_) for x_ in x]) + "]")
# print(s.canBeIncreasing(nums = x))

# # Model Solution