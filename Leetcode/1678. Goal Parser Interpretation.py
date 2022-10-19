class Solution:
    def interpret(self, command: str) -> str:
        p = 0
        c = command
        s = ""
        while p < len(c):
            if c[p] == "(":
                if c[p+1] == ")":
                    s += "o"
                    p += 2
                else:
                    q = p+1
                    while c[q] != ")":
                        q += 1
                    s += c[p+1:q]
                    p = q+1
            else:
                s += c[p]
                p += 1  
        return s