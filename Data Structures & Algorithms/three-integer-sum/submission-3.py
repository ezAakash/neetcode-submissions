class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l,r=0,len(nums)-1
        output = []
        nums.sort()
        for i,a in enumerate(nums):
            if a > 0:#ovious
                break
            
            if i > 0 and a == nums[i-1]:
                continue

            l,r=i+1,len(nums)-1
            target = -(a)
            while(l < r):
                if(nums[l]+nums[r]>target):
                    r-=1
                elif(nums[l]+nums[r]<target):
                    l+=1
                else:
                    print([nums[i],nums[l],nums[r]])
                    output.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                    #[-2,-2,0,2,2]
                
        return output           
