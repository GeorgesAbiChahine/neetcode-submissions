class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        i = 0
        j = l - 1
        max_volume = 0
        while i < j:
            left = heights[i]
            right = heights[j]

            base = j - i
            height = min(left, right)
            volume = base * height
            max_volume = max(volume, max_volume)
            if (left <= right):
                i += 1
            else:
                j -= 1
        return max_volume


        