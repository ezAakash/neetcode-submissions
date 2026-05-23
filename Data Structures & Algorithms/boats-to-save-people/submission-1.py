class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        noOfBoats = 0
        while l <= r:
            sum = people[l] + people[r]
            if sum <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
                
            noOfBoats += 1

        
        return noOfBoats

            
