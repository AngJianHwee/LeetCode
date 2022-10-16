from typing import List


class Solution:
	def isPalindrome(self, s: str) -> bool:
		new = ""
		for s_ in s:
			if s_.isalpha() or s_.isnumeric():
				new += s_.lower()
		if len(new) == 0 or len(new) == 1:
			return True
		else:
			for i in range(len(new)//2 +1):
				if new[i] != new[-1*i-1]:
					return False
			return True
		

s = Solution()
print(s.isPalindrome(s = "A man, a plan, a canal: Panama"))
print(s.isPalindrome(s = "race a car"))
print(s.isPalindrome(s = " "))
