import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [] 
        heapq.heapify(self.heap)
        self.create_max_heap(nums)

    def create_max_heap(self, nums):
        for num in nums:
            heapq.heappush(self.heap, -num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        largest = -heapq.nsmallest(self.k, self.heap)[self.k - 1]
        return largest
