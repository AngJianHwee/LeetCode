class Solution:
    def arraySign(self, nums: List[int]) -> int:
        positive = True
        for num in nums:
            if num == 0:
                return 0
            if num <0:
                positive = not positive
        if positive:
            return 1
        return -1