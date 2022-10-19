class Solution:
    def minTimeToType(self, word: str) -> int:
        c = 0
        p = ord('a')
        for w in word:
            c += min(abs(p-ord(w)),abs(p+26-ord(w)),abs(p-26-ord(w))) + 1
            p = ord(w)
        return c
        