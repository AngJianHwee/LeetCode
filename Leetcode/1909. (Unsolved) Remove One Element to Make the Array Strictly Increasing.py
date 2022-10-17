from typing import List


class Solution:


    def canBeIncreasing(self, nums: List[int]) -> bool:
        def isIncreasing(arr):
            if len(arr) == 0:
                return True
            if len(arr) == 1:
                return True
            else:
                for i in range(len(arr)-1):
                    if arr[i] >= arr[i+1]:
                        return False
                return True
        
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                if i == 0:
                    return isIncreasing(nums[1:])
                if i == (len(nums)-1):
                    return isIncreasing(nums[:-1]) or isIncreasing(nums[:-2] + [nums[-1]])
                else:
                    return isIncreasing(nums[:i] + nums[i+1:]), isIncreasing(nums[:i-1] + nums[i:])




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