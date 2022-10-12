from typing import List
class Solution:
    def isUgly(self, n: int) -> bool:  
        if n <0:
            return False
        
        if n == 0:
            return False
        
        if n == 1:
            return True
        current = 2
        
        while current <= abs(n):
            if current > 5:
                return False
            
            if n % current == 0:
                n = int(n/current)
                current = 2
            else:
                current += 1
        return True

s = Solution()
print(s.isUgly(-2147483648))


# # Model Solution
# class Solution:
#     def isUgly(self, num: int) -> bool:
#         if num == 0: return False
#         while num % 5 == 0: num /= 5
#         while num % 3 == 0: num /= 3
#         while num % 2 == 0: num /= 2
#         return num == 1