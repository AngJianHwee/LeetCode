class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w[::-1] == w:
                return w
        return ""
        