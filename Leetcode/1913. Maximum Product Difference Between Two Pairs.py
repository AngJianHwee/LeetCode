class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        x = sorted(nums)
        return x[-1]*x[-2] - x[0]*x[1]
        