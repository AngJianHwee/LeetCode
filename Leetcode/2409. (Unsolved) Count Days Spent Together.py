from typing import List


class Solution:

	def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
		def toAbs(date: str):
			month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
			arr = [int(x) for x in date.split("-")]
			return sum(month[:arr[0]+1]) + arr[1]

		arriveAlice = toAbs(arriveAlice)
		leaveAlice = toAbs(leaveAlice)
		arriveBob = toAbs(arriveBob)
		leaveBob = toAbs(leaveBob)
		

		return max(min(leaveAlice,leaveBob) - max(arriveAlice, arriveBob)+1,0)



s = Solution()
print(s.countDaysTogether(arriveAlice="08-15",
						  leaveAlice="08-18", arriveBob="08-16", leaveBob="08-19"))
print(s.countDaysTogether(arriveAlice="10-01",
						  leaveAlice="10-31", arriveBob="11-01", leaveBob="12-31"))
print(s.countDaysTogether("10-20", "12-22", "06-21", "07-05"))

# # Model Solution
