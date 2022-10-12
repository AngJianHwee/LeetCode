class Solution:
    def reverse(self, x: int) -> int:
        is_negative = 0
        if x < 0:
            is_negative = 1
            x = x * -1

        arr = []
        while x != 0:
            arr.append(x % 10)
            x = int(x/10)

        ans = 0
        for _ in arr:
            ans = ans*10 + _
        if is_negative:
            ans = ans*(-1)
        
        return ans


x = Solution()
print(x.reverse(12345))
print(x.reverse(-12345))
