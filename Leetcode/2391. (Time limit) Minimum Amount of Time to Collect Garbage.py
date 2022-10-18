from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def defaultDictCount(arr):
            dic = {}
            for x in arr:
                try:
                    dic[x] += 1
                except:
                    dic[x] = 1
            for x in ["G","P","M"]:
                try:
                    dic[x]
                except:
                    dic[x] = 0
            return [dic['G'],dic['P'],dic['M']]

        G, P, M = [], [], []
        for gar in garbage:
            g,p,m = defaultDictCount(gar)
            G.append(g)
            P.append(p)
            M.append(m)
        t = 0
        for a in [G, P, M]:
            for i in range(len(a)):
                if sum(a[i:]) == 0:
                    break
                t += a[i]
                if i != 0:
                    t += travel[i-1]
        return t




s = Solution()
print(s.garbageCollection(garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3]))
print("Answer: 21")
print(s.garbageCollection(garbage=["MMM", "PGM", "GP"], travel=[3, 10]))
print("Answer: 37")
# print("Answer: 37")