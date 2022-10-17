from typing import List


# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         def defaultDictCount(arr):
            
#             dic = {}
#             for x in arr:
#                 try:
#                     dic[x] += 1
#                 except:
#                     dic[x] = 1
#             dic = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)
#             return dic

#         s = ""
#         for p in paragraph:
#             if p.isalpha() or p == " ":
#                 s += p
#             else:
#                 s += " "
#         paragraph = s.lower()
#         arr = [x.strip() for x in paragraph.strip().split() if x != "" and x not in banned]
#         dic = defaultDictCount(arr)
#         return (dic[0][0])



# # Better 
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         def defaultDictCount(arr):
            
#             dic = {}
#             for x in arr:
#                 try:
#                     dic[x] += 1
#                 except:
#                     dic[x] = 1
#             # dic = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)
#             return dic

#         s = ""
#         for p in paragraph:
#             if p.isalpha() or p == " ":
#                 s += p
#             else:
#                 s += " "
#         paragraph = s.lower()
#         arr = [x.strip() for x in paragraph.strip().split() if x != "" and x not in banned]
#         dic = defaultDictCount(arr)

#         val, val_value = 0,0
#         for x,y in dic.items():
            
#             if y > val_value:
#                 val = x
#                 val_value = y

#         return val


# Even Better, but slower
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        def defaultDictCount(arr):
            
            dic = {}
            for x in arr:
                try:
                    dic[x] += 1
                except:
                    dic[x] = 1
            # dic = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)
            return dic

        s = ""
        for p in paragraph:
            if p.isalpha() or p == " ":
                s += p
            else:
                s += " "
        paragraph = s.lower()
        arr = [x.strip() for x in paragraph.strip().split() if x != "" and x not in banned]
        dic = defaultDictCount(arr)

        return max(dic, key=dic.get)



s = Solution()
print(s.mostCommonWord(paragraph = "a.", banned = []))
print(s.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
print(s.mostCommonWord("a, a, a, a, b,b,b,c, c",["a"]))
