class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        def defaultDictCount(arr):
            dic = {}
            for x in arr:
                try:
                    dic[x] += 1
                except:
                    dic[x] = 1
            return dic    
        return sorted(defaultDictCount(nums).items(), key = lambda x: x[1], reverse = True)[0][0]