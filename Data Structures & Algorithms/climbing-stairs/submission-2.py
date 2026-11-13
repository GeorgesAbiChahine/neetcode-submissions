class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[0] = 1
        memo[1] = 1

        def dfs(k):
            if k in memo:
                return memo[k]
            memo[k] = dfs(k - 1) + dfs(k - 2)
            return memo[k]

        return dfs(n)