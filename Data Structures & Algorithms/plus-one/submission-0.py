class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        n = len(digits)
        
        for i, digit in enumerate(digits):
            num += digit * (10 ** (n - 1 - i))
        
        num += 1
        return [int(d) for d in str(num)]
        