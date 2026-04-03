class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = []
        counts = Counter(nums)
        for i in range(0,k):
            frequent.append(max(counts, key=counts.get))
            del counts[max(counts, key=counts.get)]
        return frequent