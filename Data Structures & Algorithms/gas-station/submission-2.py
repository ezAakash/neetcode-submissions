class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        N = len(gas)

        total_gas = 0
        res = N
        for i in range(len(gas)):
            total_gas += gas[i]
            if total_gas - cost[i] < 0:
                res = N
                total_gas = 0
                continue
            
            total_gas -= cost[i]
            res = min(res, i)
        
        return res