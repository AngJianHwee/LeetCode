class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        x = ["type","color","name"]
        i = x.index(ruleKey)
        return len([x for x in items if x[i] == ruleValue])
        