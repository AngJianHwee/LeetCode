class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            arr.append(sum([int(x) for x in bin(i)[2:]]))
        return arr