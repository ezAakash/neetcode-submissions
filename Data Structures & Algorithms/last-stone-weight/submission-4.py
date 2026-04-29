class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            new_weight = first - second 
            if new_weight != 0:
                heapq.heappush(stones, -new_weight)
        
            
        return abs(stones[0]) if stones else 0