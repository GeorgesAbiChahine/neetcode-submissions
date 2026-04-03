class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        for num in numbers:
            if i == j:
                break
            x = numbers[i] + numbers[j]
            if x == target:
                return [i+1, j+1]
            elif x > target:
                j -= 1
            elif  x < target:
                i += 1
        return []