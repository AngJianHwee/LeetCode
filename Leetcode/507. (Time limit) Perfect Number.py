from typing import List


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        div = []
        if num == 1:
            return True
        elif num == 2:
            return False

        for i in range(1, num//2+1):
            if num % i == 0:
                div.append(i)
        return sum(div) == num


s = Solution()
print(s.checkPerfectNumber(28))
print(s.checkPerfectNumber(7))

# # Model Solution
