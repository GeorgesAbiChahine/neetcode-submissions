class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        last_seen = {}
        first = 0
        max_len = 0

        for i, ch in enumerate(s):
            if ch in last_seen:
                first = max(first, last_seen[ch] + 1)
            last_seen[ch] = i
            max_len = max(max_len, i - first + 1)

        return max_len
