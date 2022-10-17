from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        x = sorted(nums)
        return [i for i in range(len(x)) if x[i] == target]
