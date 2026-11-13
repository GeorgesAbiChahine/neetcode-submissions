class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return -1
        elif len(nums) == 1:
            return nums[0]
        memo = {}
        memo[0] = nums[0]

        memo[1] = max(nums[0], nums[1])
        def dp(i):
            if i not in memo:
                memo[i] = max(dp(i-1), nums[i] + dp(i-2))
            return memo[i] 
        return dp(len(nums) - 1)

        