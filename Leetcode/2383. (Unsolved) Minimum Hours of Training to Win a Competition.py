from typing import List


class Solution:
	def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
		extraEnergy = 0
		extraExperience = 0
		for i in range(len(energy)):
			if initialEnergy < energy[i]:
				extraEnergy += initialEnergy - energy[i] + 1
				initialEnergy = energy[i] + 1
			initialEnergy -= energy[i]

			if initialExperience < experience[i]:
				extraExperience += initialExperience - experience[i] + 1
				initialExperience = experience[i] + 1
			initialExperience += experience[i]
		return extraEnergy, extraExperience


s = Solution()
print(s.minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1, 4,3,2], experience = [2,6,3,1]))
print(s.minNumberOfHours(initialEnergy= 2, initialExperience = 4, energy = [1], experience = [3]))

# # Model Solution
