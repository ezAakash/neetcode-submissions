class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = [(abs(a - x), a) for a in arr]

        heapq.heapify(diff)
        
        res = []
        while k > 0:
            res.append(heapq.heappop(diff)[1])
            k -= 1
        
        return sorted(res)