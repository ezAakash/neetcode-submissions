class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for val in arr:
            distance = abs(val - x)
            heapq.heappush(heap, (-distance, -val))

            if len(heap) > k:
                heapq.heappop(heap)
            
        
        res = [- val for (_, val) in heap]

        return sorted(res)