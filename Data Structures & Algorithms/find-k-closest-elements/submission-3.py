class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        diff = []
        for num in arr:
            heapq.heappush(diff, (-1 * abs(x - num), -1 * num))

            if len(diff) > k:
                heapq.heappop(diff)
        
        res = []

        for _, num in diff:
            res.append(-1 * num)
        
        res.sort()
        return res
        


        

