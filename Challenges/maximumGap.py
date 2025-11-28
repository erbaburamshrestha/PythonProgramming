def maximumGap(nums):
        if len(nums)==0:
            return 0
        
        difference=0
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]>difference:
                difference=nums[i+1]-nums[i]  
            else:
                difference
                
        return difference
        
nums = [3,6,9,1]
print(maximumGap(nums))
nums2=[10]
print(maximumGap(nums2))
