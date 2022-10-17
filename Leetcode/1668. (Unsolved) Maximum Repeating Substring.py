from typing import List


class Solution:
	def maxRepeating(self, sequence: str, word: str) -> int:
		n = 0
		i = 0
		while i < len(sequence):
			cur_n = 0
			while sequence[i:i+len(word)] == word:
				i += len(word)
				cur_n += 1
			n = max(n,cur_n)
			i += 1
		return n

		

s = Solution()
print(s.maxRepeating(sequence = "ababc", word = "ab"))
print(s.maxRepeating(sequence = "ababc", word = "ba"))
print(s.maxRepeating(sequence = "ababc", word = "ac"))
