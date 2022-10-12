from typing import List


class Solution:
	def countEven(self, num: int) -> int:
		if num == 0:
			return 0
		if num == 1:
			return 0
		if num == 2:
			return 1
		if num == 3:
			return 1
		if num == 4:
			return 2

		count = 0
		for i in range(1,num+1):
			if sum([int(x) for x in str(i)])%2 == 0:
				count +=1
		return count

s = Solution()
print(s.countEven(4))
print(s.countEven(4000))
