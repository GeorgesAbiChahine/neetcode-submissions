class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        DP = [False] * (n + 1)
        DP[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i] in wordDict and DP[j] == True:
                    DP[i] = True

        return DP[n]
        