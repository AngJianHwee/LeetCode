class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a = [x for x in nums if x%2 == 0]
        b = [x for x in nums if x%2 == 1]
        return a+b
        