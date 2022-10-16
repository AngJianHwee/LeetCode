from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(min([len(x) for x in strs])):
            x = strs[0][i]
            for j in range(len(strs)):
                if x != strs[j][i]:
                    return strs[0][:i]
        return strs[0][:min([len(x) for x in strs])]


s = Solution()
print(s.longestCommonPrefix(strs=["flower", "flow", "flight"]))
print(s.longestCommonPrefix(strs=["dog", "racecar", "car"]))

# # Model Solution
# class Solution:
#     def longestCommonPrefix(self, S: List[str]) -> str:
#         if not S: return ''
#         m, M, i = min(S), max(S), 0
#         for i in range(min(len(m),len(M))):
#             if m[i] != M[i]: break
#         else: i += 1
#         return m[:i]