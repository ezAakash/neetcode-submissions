class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # question 1 : different triplets means : any two .
        # do we need to make the target from only two things i and j --> target just like 2 sum problem .
        # supposing we can only take two at a time 

        # let's sort 1,4,4 2,5,6 5,7,5

        x = y = z = False

        for t in triplets:
            x |= (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])
            y |= (t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2])
            z |= (t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2])
        
        if x and y and z:
            return True
        
        return False
        