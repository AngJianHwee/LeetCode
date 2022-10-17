from typing import List


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        if len(s1) == 1:
            return s1 == s2

        if len(s1) == 2:
            return s1 == s2[::-1]

        # def defaultDictCount(arr):
        #     dic = {}
        #     for x in arr:
        #         try:
        #             dic[x] += 1
        #         except:
        #             dic[x] = 1
        #     dic = sorted(dic.items(), key=lambda kv: kv[1])
        #     return dic

        # st1 = set(defaultDictCount(s1))
        # st2 = set(defaultDictCount(s2))
        # return not bool(len(st1 - st2))

        diff = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff == -1:
                    diff = i
                elif diff == -2:
                    return False
                else:
                    if (s1[diff] == s2[i]) and (s2[diff] == s1[i]):
                        diff = -2
                    else:
                        return False
        return diff == -2


s = Solution()
print(s.areAlmostEqual(s1="bank", s2="kanb"))
print(s.areAlmostEqual(s1="attack", s2="defend"))
print(s.areAlmostEqual(s1="kelb", s2="kelb"))
print(s.areAlmostEqual(s1="a", s2="b"))
print(s.areAlmostEqual(s1="ab", s2="ba"))
print(s.areAlmostEqual("npv","zpn"))
print(s.areAlmostEqual("abca","abcc"))

