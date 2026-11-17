class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        DP = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        best = 0

        def dp(i,j):
            if text1[i - 1] == text2[j - 1]:
                DP[i][j] = DP[i-1][j-1] + 1
                best = DP[i][j]
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        for i in range(1,n+1):
            for j in range(1, m+1):
                dp(i,j)
        return DP[n][m]



        