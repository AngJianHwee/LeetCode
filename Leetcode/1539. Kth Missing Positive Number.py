from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr.append(arr[-1]+k+2)
        missing = []
        p = 0
        j = 1
        while len(missing) != k:
            while arr[p] < j:
                p += 1
            if j < arr[p]:
                missing.append(j)
            j += 1
        return missing[-1]


        
s = Solution()
print(s.findKthPositive(arr = [2,3,4,7,11], k = 5))
print(s.findKthPositive(arr = [1,2,3,4], k = 2))
