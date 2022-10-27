class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[2:]
        while len(x) < 32:
            x = '0' + x
        return int(x[::-1],2)
        