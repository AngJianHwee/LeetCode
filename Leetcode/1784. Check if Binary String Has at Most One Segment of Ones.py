from typing import List


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0 
        i = 0
        while i < len(s):
            print(i)
            if s[i] == "1":
                count += 1
                while i < len(s) and s[i] == '1':
                    i += 1
            i += 1            
        return count == 1 


s = Solution()
print(s.checkOnesSegment(s="1001"))
print(s.checkOnesSegment(s="110"))

# Model Solution
