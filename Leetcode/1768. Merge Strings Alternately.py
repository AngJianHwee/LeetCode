class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        p1 = 0
        p2 = 0
        while p1 + p2 < (len(word1) + len(word2)):
            try:
                s += word1[p1]
                p1 += 1
            except Exception as e:
                None                

            try:
                s += word2[p2]
                p2 += 1
            except Exception as e:
                None                
        return s

s = Solution()
print(s.mergeAlternately("ab","pqrs"))