from typing import List
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dic = {}
        for x,y in knowledge:
            knowledge_dic[x] = y
        new_s = ''
        i = 0
        while i <len(s):
            if s[i] != "(":
                new_s += s[i]
                i+=1
            else:
                j = i+1
                while s[j]!=")":
                    j+=1
                try:
                    new_s += knowledge_dic[s[i+1:j]]
                except:
                    new_s += '?'
                i = j+1
        return new_s

s = Solution()
print(s.evaluate(s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]))
print(s.evaluate(s = "hi(name)", knowledge = [["a","b"]]))
print(s.evaluate(s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]))
