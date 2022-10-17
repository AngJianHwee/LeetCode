from typing import List

class Solution:
    def minPartitions(self, n: str) -> int:
        print(int(n) - 1*10**(len(str(n))-1))

s = Solution()
print(s.minPartitions(n = "32"))
print(s.minPartitions(n = "82734"))
print(s.minPartitions(n = "27346209830709182346"))



# greedy least sum of digit