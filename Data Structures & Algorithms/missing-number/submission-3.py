class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        self.merge_sort(nums)
 
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        
        return i + 1
    def merge_sort(self, arr):
        if len(arr) > 1:
            # Step 1: Find the midpoint and split the array
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Step 2: Recursively sort both halves
            self.merge_sort(left_half)
            self.merge_sort(right_half)

            # Step 3: Merge the sorted halves
            i = j = k = 0

            # Compare elements from left_half and right_half
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            # Collect any remaining elements from left_half
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            # Collect any remaining elements from right_half
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1        