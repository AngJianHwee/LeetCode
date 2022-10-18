class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        kadane = [nums[0]]
        for i in range(1,len(nums)):
            kadane.append(max(kadane[-1],0)+ nums[i])
        return max(kadane)
        
        