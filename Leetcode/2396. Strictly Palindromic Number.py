from typing import List


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        DP = [-1 for j in range(int(n+1))]
        DP[1] = 1

        def dp(n, arr):
            if arr[n] != -1:
                return arr[n]

            s = str(bin(n))[2:]

            if len(s) == 1:
                arr[n] = 1
                return arr[n]

            elif len(s) == 2:
                arr[n] = int(s == s[::-1])
                return arr[n]

            else:
                if s[0] == s[-1]:
                    arr[n] = dp(int(s[1:-1], 2), arr)
                    return arr[n]
                else:
                    arr[n] = 0
                    return arr[n]

        for i in range(n+1):
            if not bool(dp(i, DP)):
                return False
        return True


# # Model Solution
# # Explanation : There is no as such number/term possible so simply return false.
# class Solution:
#     def isStrictlyPalindromic(self, n: int) -> bool:
#         return False;
#

s = Solution()
print(s.isStrictlyPalindromic(n=9))
