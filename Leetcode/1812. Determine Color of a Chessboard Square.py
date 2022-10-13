class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if ord(coordinates[0])%2 == 0:
            return bool(int(coordinates[1])%2)
        else:
            return bool((int(coordinates[1])+1)%2)

s = Solution()
print(s.squareIsWhite(coordinates = "a1"))
print(s.squareIsWhite(coordinates = "h3"))
print(s.squareIsWhite(coordinates = "c7"))
