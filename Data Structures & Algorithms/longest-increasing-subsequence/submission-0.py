class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        DP = [1] * n

        def dp(i):
            for j in range(i):
                if nums[i] > nums[j]:
                    DP[i] = max(DP[i], DP[j] + 1)

        for i in range(n):
            dp(i)

        return max(DP)