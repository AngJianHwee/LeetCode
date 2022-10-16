from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        dic2 = {}
        if len(pattern) != len(s.split()):
            return False
        for x, y in list(zip(pattern, s.split())):
            if x in dic.keys():
                if dic[x] != y:
                    return False
            else:
                dic[x] = y

            if y in dic2.keys():
                if dic2[y] != x:
                    return False
            else:
                dic2[y] = x
        return True


s = Solution()
print(s.wordPattern(pattern="abba", s="dog cat cat dog"))
print(s.wordPattern(pattern="abba", s="dog cat cat fish"))
print(s.wordPattern(pattern="aaaa", s="dog cat cat dog"))

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
