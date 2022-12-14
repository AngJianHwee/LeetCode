class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        mr = [max(x) for x in grid]
        mc = [max([grid[i][j] for i in range(len(grid)) ])for j in range(len(grid[0]))]
        
        t = 0
        for i in range(len(grid)):
             for j in range(len(grid[0])):
                    if (grid[i][j] == mr[i]) or (grid[i][j] == mc[j]):
                        continue
                    t += abs(grid[i][j] - min(mr[i],mc[j]))
        return t


# # Two-liner
# class Solution:
#     def maxIncreaseKeepingSkyline(self, G: List[List[int]]) -> int:
#         M, N, R, C = len(G), len(G[0]), [max(r) for r in G], [max(c) for c in zip(*G)]
#         return sum(min(R[i],C[j]) - G[i][j] for i,j in itertools.product(range(M),range(N)))