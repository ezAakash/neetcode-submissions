class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        noOfBoats = 0
        while l <= r:
            sum = people[l] + people[r]
            if sum <= limit:
                noOfBoats += 1
                l += 1
                r -= 1
            else:
                noOfBoats += 1
                r -= 1
        
        return noOfBoats
        
            
