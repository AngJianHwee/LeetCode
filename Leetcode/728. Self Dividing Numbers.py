class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for i in range(left, right+1):
            if '0' in str(i):
                continue
            if sum([i%int(x_) for x_ in str(i)]) == 0:
                arr.append(i)
        return arr
