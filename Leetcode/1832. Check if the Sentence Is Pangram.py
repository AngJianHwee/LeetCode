from typing import List

class Solution:
	def checkIfPangram(self, sentence: str) -> bool:
		def defaultDictCount(arr):
			dic = {}
			for x in arr:
				if not x.isalpha():
					continue
				try:
					dic[x]
				except:
					dic[x] = 1
			
			return dic
		if len(defaultDictCount(sentence).keys()) != 26:
			return False
		return True


s = Solution()
print(s.checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog"))
print(s.checkIfPangram(sentence = "leetcode"))