class Solution:
    def replaceDigits(self, s: str) -> str:
        t = []
        for i in range(len(s)):
            if s[i].isdigit():
                t.append(chr(ord(s[i-1])+int(s[i])))
            else:
                t.append(s[i])
        return "".join(t)