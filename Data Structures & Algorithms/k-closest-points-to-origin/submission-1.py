import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        
        for (x, y) in points:
            distance = x**2 + y**2  # squared distance
            # push as (-distance, [x, y]) to make it a max heap
            heapq.heappush(heap, (-distance, [x, y]))
            
            # if we have more than k points, remove the farthest
            if len(heap) > k:
                heapq.heappop(heap)
        
        # extract just the points
        return [point for (_, point) in heap]
