# from typing import List


# class Solution:
#     def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
#         dic = {}
#         for x, y in logs:
#             try:
#                 dic[x] = min(y, dic[x])
#             except:
#                 dic[x] = y

#         arr = [0 for i in range(k)]
#         for x,y in dic.items():
#             arr[y-1] += 1
#         return arr


# s = Solution()
# print(s.findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5))
# print(s.findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4))
# # # Model Solution



X = [-0.15, 8.6, 5.0, 3.71, 4.29, 7.74, 2.48, 3.25, -1.15, 8.38]
Y = [2.55, 12.07, 0.46, 0.35, 2.69, -0.94, 1.73, 0.73, -0.35, -0.37]
print(sorted(X))
print(sorted(Y))
print(sorted(X+Y))