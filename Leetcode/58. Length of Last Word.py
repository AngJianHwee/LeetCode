from typing import List


class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		arr = [x.strip().lower() for x in s.strip().split() if x != ""]
		if len(arr) == 0:
			return 0
		return len(arr[-1])


s = Solution()
print(s.lengthOfLastWord(s = "Hello World"))
print(s.lengthOfLastWord(s = "   fly me   to   the moon  "))
print(s.lengthOfLastWord(s = "luffy is still joyboy"))
