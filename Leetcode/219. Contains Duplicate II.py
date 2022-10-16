from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            try:
                if abs(i - dic[nums[i]]) <= k:
                    return True
                dic[nums[i]] = i
            except:
                dic[nums[i]] = i
        return False


# # Time Limit
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, min(i+k+1, len(nums))):
#                 if nums[i] == nums[j]:
#                     return True
#         return False


s = Solution()
print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
print(s.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))

# # Model Solution
