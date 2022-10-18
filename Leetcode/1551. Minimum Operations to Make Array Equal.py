class Solution:
    def minOperations(self, n: int) -> int:
        x = [2*i + 1 for i in range(n)]
        mean = (sum(x)//n)
        y = [2*i + 1 for i in range(n)]
        tot = 0
        for y_ in y:
            tot += abs(y_ - mean)
        return tot//2
        