class Solution:    
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        return self.b_s(nums, target, left, right)

    def b_s(self, nums, target, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
            return self.b_s(nums, target, left, right - 1)
        else:
            left = mid
            return self.b_s(nums, target, left + 1, right)
        
            





        