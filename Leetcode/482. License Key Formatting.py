from typing import List


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
        s = s[::-1]
        arr = [s[k*i:k*i+k] for i in range(len(s)//k+1)]
        arr = [x for x in arr if x.strip() != ""]
        return "-".join(arr).upper()[::-1]


s = Solution()
s.licenseKeyFormatting("5F3Z-2e-9-w-w", 4)
