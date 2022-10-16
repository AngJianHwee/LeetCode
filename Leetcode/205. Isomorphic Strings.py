from typing import List


class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		dic = {}
		for i in range(len(s)):
			if s[i] in list(dic.keys()):
				if dic[s[i]] != t[i]:
					return False
			else:
				dic[s[i]] = t[i]
				if len(list(dic.values())) != len(set(list(dic.values()))):
					return False
		return True


s = Solution()
print(s.isIsomorphic(s="egg", t="add"))
print(s.isIsomorphic(s="foo", t="bar"))
print(s.isIsomorphic(s="paper", t="title"))
print(s.isIsomorphic("badc", "baba"))

# # Model Solution
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         zipped_set = set(zip(s, t))
#         return len(zipped_set) == len(set(s)) == len(set(t))