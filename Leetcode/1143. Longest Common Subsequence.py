class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dpr = [[-1 for i in range(max(len(text1), len(text2))+1)] for j in range(max(len(text1), len(text2))+1)]
        def dp(s1,s2,p1,p2, dpr):
            if dpr[p1][p2] != -1:
                return dpr[p1][p2]
            if p1 == len(s1) or p2 == len(s2):
                dpr[p1][p2] = 0
                return 0
            if s1[p1] == s2[p2]:
                dpr[p1][p2] = 1 + dp(s1,s2,p1+1,p2+1,dpr)
                return dpr[p1][p2]
            else:
                dpr[p1][p2] = max(dp(s1,s2,p1+1,p2,dpr),dp(s1,s2,p1,p2+1,dpr))
                return dpr[p1][p2]
        return dp(text1,text2,0,0,dpr)