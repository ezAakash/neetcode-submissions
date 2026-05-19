class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        

        total_gas = 0
        res = len(gas)
        for i in range(len(gas)):
            total_gas += gas[i]
            if total_gas - cost[i] < 0:
                res = len(gas)
                total_gas = 0
                continue
            
            total_gas -= cost[i]
            res = min(res, i)
        
        return res