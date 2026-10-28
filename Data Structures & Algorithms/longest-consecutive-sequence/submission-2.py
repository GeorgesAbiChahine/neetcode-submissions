class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            len = 0
            if num - 1 not in numSet:
                len = 1
                while num + len in numSet:
                    len += 1
            longest = max(longest,len)
        return longest