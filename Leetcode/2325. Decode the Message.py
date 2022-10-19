class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        k = []
        for x in key:
            if x not in k and x.isalpha():
                k.append(x)
        m = ""
        for y in message:
            if y.isalpha():
                m += chr(k.index(y) + ord('a'))
            else:
                m += y
        return m
        