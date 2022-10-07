from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = []
        i = 0
        j = 0
        while i + j != len(nums1) + len(nums2):
            print(i, j)
            if i == len(nums1):
                nums3.extend(nums2[j:])
                break
            elif j == len(nums2):
                nums3.extend(nums1[i:])
                break

            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        if len(nums3)%2 == 0:
            return (float(nums3[int(len(nums3)/2)]) + float(nums3[int(len(nums3)/2)-1]))/2
        else:
            return float(nums3[int(len(nums3)/2)])
