from typing import List


class Solution:
	def isLongPressedName(self, name: str, typed: str) -> bool:
		i = 0
		j = 0

		while i < len(name):
			if name[i] == typed[j]:
				x = name[i]
				p = 0
				q = 0
				i+=1
				j+=1
				while i < len(name) and name[i] == x:
					p += 1
					i += 1
				while j < len(typed) and typed[j] == x:
					q += 1
					j += 1
				if p > q:
					return False
			else:
				return False
		return True

				


s = Solution()
print(s.isLongPressedName(name = "alex", typed = "aaleex"))
print(s.isLongPressedName(name = "saeed", typed = "ssaaedd"))
print(s.isLongPressedName("xnhtq","xhhttqq"))
