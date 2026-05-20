class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # question 1 : different triplets means : any two .
        # do we need to make the target from only two things i and j --> target just like 2 sum problem .
        # supposing we can only take two at a time 

        # let's sort 1,4,4 2,5,6 5,7,5

        valid_triplets = []
        x, y, z = target

        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue
            valid_triplets.append([a, b, c])
        
        max_a, max_b , max_c = 0, 0 , 0

        for a, b , c in valid_triplets:
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            max_c = max(max_c, c)
        
        return True if max_a == x and max_b == y and max_c == z else False