from typing import List


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        arr = perm.copy()
        i = 1
        while True:
            if i%2 == 1:
                arr[i] = perm[int(n / 2 + (i - 1) / 2)]
            else:
                arr[i] = perm[int(i / 2)]
            
            if (arr == perm):
                break
            i+=1

        print(arr,i)

s = Solution()
s.reinitializePermutation(5)