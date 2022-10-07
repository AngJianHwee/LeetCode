from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for x in nums:
            if x == target:
                return nums.index(x)
        if nums[0] > target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        
        else:
            for i in range(len(nums)-1):
                if nums[i] < target < nums[i+1]:
                    return i+1
                