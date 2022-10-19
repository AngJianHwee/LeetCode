class Solution:
    def sortString(self, s: str) -> str:
        def dicCount(ss):
            dic = {}
            for s in ss:
                try:
                    dic[s] += 1
                except:
                    dic[s] = 1
            return dic
        
        def join(dic):
            s = ""
            for x,y in dic.items():
                s += x*y
            return s
        
        t = ""
        
        dic = dicCount(s)
        while len(dic.keys()) > 0:
            t += "".join(sorted(dic.keys()))
            for x in dic.keys():
                dic[x] -= 1
            dic = dicCount(join(dic))       
            t += "".join(sorted(dic.keys()))[::-1]
            for x in dic.keys():
                dic[x] -= 1
            dic = dicCount(join(dic))       
        
        return t
