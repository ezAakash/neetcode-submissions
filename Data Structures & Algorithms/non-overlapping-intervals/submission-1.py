class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        min_count = 0
        intervals.sort(key = lambda pair: pair[0])

        last_end = float('-inf')
        for start, end in intervals:
            if last_end > start:#overlapping region
                min_count += 1
                last_end = min(last_end, end)
            else:
                last_end = end
                

        return min_count 


