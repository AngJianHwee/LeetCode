from typing import List


# class Solution:
#     def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
#         for i in range(len(dominoes)):
#             dominoes[i] = sorted(dominoes[i])
#         count = 0


#         def defaultDictCount(arr):
#             dic = {}
#             for x in arr:
#                 try:
#                     dic[str(x)] += 1
#                 except:
#                     dic[str(x)] = 1

#             return dic

#         def nCrModp(n, r, p):
#             C = [0 for i in range(r + 1)]

#             C[0] = 1 # Top row of Pascal Triangle

#             # One by constructs remaining rows of Pascal
#             # Triangle from top to bottom
#             for i in range(1, n + 1):

#                 # Fill entries of current row
#                 # using previous row values
#                 for j in range(min(i, r), 0, -1):

#                     # nCj = (n - 1)Cj + (n - 1)C(j - 1)
#                     C[j] = (C[j] + C[j-1]) % p

#             return C[r]

#         dic = defaultDictCount(dominoes)
#         count = 0
#         for x, y in dic.items():
#             if y > 1:
#                 count += (nCrModp(y,2,int(1e18)))
#         return count

# Better
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for i in range(len(dominoes)):
            dominoes[i] = sorted(dominoes[i])
        count = 0

        def defaultDictCount(arr):
            dic = {}
            for x in arr:
                try:
                    dic[str(x)] += 1
                except:
                    dic[str(x)] = 1

            return dic

        dic = defaultDictCount(dominoes)
        count = 0
        for x, y in dic.items():
            count += int(y*(y-1)/2)
        return count


s = Solution()
print(s.numEquivDominoPairs(dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]]))
print(s.numEquivDominoPairs(dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))
