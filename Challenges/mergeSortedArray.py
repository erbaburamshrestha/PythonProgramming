def mergeList(nums1,m,nums2,n):
    mergeLst = sorted(nums1[:m] + nums2)
    return mergeLst

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(mergeList(nums1,m,nums2,n))
