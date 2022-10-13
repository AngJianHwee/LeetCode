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

for i in range(int(input())):
    arr = [int(x) for x in input().split()[1:]]
    count = 0
    for x in arr:
        if x > sum(arr)/len(arr):
            count += 1
    print(f"{count/len(arr)*100:.3f}%")