class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x = word.find(ch)
        return word[:x+1][::-1] + word[x+1:]
        