from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)

# # Using 1 dict
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         dic = {}
#         for x in nums1:
#             try:
#                 dic[x]
#             except:
#                 dic[x] = 1
#         for x in nums2:
#             try:
#                 if dic[x] == 1:
#                     dic[x] = 0
#             except:
#                 dic[x] = -1
        
#         return [x for x, y in dic.items() if y == 0]

s = Solution()
print(s.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print(s.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
 
 