from typing import List


class Solution:
	def maximumTime(self, time: str) -> str:
		arr = [x for x in time]
		if arr[0] == "?":
			if arr[1] == "?":
				arr[0] = "2"
			elif int(arr[1]) >= 4:
				arr[0] = "1"
			else:
				arr[0] = "2"
		if arr[1] == "?":
			if arr[0] == "2":
				arr[1] = "3"
			else:
				arr[1] = "9"
		if arr[3] == "?":
			arr[3] = "5"
		if arr[4] == "?":
			arr[4] = "9"
		return "".join(arr)

		


s = Solution()
print(s.maximumTime(time = "0?:3?"))
print(s.maximumTime(time = "2?:?0"))
print(s.maximumTime(time = "1?:22"))
print(s.maximumTime(time = "?4:03"))

# # Model Solution
