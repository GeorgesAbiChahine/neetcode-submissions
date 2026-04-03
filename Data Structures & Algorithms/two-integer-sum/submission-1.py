class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        couple = []
        j = 0
        for i in range(0, len(nums)):
            if (target - nums[i]) in nums and i != nums.index(target - nums[i]):
                j = nums.index(target - nums[i])
                break
        
        if i > j :
            couple = [j, i]
        else:
            couple = [i, j]

        return couple
            

    