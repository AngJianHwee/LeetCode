from typing import List


class Solution:
    def equalFrequency(self, word: str) -> bool:
        dic = {}
        for w in word:
            if w in dic.keys():
                dic[w] += 1
            else:
                dic[w] = 1
        if len([x for x in dic.values() if x == 1]) == 1:
            return True
        x = (sum(dic.values())-1)/len(dic.keys())
        return abs(x - int(x)) < 1e-5



s = Solution()
print(s.equalFrequency(word = "abcc"))
print(s.equalFrequency(word = "aazz"))
print(s.equalFrequency(word = "bac"))
print(s.equalFrequency(word = "ddaccb"))
print(s.equalFrequency(word = "bac"))



# # Model Solution
# def wordPattern(self, pattern, str):
#     s = pattern
#     t = str.split()
#     return map(s.find, s) == map(t.index, t)

# def wordPattern(self, pattern, str):
#     f = lambda s: map({}.setdefault, s, range(len(s)))
#     return f(pattern) == f(str.split())

# def wordPattern(self, pattern, str):
#     s = pattern
#     t = str.split()
#     return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
