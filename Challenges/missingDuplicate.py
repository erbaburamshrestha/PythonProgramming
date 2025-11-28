def missingDuplicate(nums):
    lengthNums=len(nums)
    result = nums[0]
    for i in range(1,lengthNums):
        result = result ^ nums[i] # xor gives the missing duplicate in python
     
    return result
 
nums = [4,1,2,1,2,]
print(missingDuplicate(nums))