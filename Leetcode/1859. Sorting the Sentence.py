class Solution:
    def sortSentence(self, s: str) -> str:
        x = s.split()
        y = ["" for _ in range(len(x))]
        for x_ in x:
            j = -1
            while x_[j].isdigit():
                j-=1
            y[int(x_[j+1:])-1] = x_[:j+1]
        return " ".join(y)
            