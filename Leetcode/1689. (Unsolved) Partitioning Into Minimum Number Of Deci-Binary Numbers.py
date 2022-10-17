class Solution:
    def minPartitions(self, n: str) -> int:
        j = 1
        bin_arr = [1,2,4,8]
        while bin_arr[-1] < n:
            bin_arr.append(bin_arr[-1]*2)

        count = 0
        for x in bin_arr[::-1]:
            while n > x:
                n -= x
                count += 1
                