class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        mr = [max(x) for x in grid]
        mc = [max([grid[i][j] for i in range(len(grid)) ])for j in range(len(grid[0]))]
        
        t = 0
        for i in range(len(grid)):
             for j in range(len(grid[0])):
                    if (grid[i][j] == mr[i]) or (grid[i][j] == mr[j]):
                        continue
                    t += abs(min(mr[i],mr[j]) - grid[i][j])
        print(t)