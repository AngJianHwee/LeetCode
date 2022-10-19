class Solution:
    def countAsterisks(self, s: str) -> int:
        st = True
        c = 0
        for s_ in s:
            if s_ == "|":
                st = not st
            if s_ == "*" and st:
                c += 1
        return c