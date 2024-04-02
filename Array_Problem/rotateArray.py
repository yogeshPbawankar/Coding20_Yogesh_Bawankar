def rotateArray(nums,k):
    i = k
    for i in range(len(nums)):
        for j in range(k,len(nums)-1):
            if nums[j] < nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
"""
# Optimize Approch 
    nums[k:]= sorted(nums[k:],reverse = True)
    return nums
"""
nums = [1,2,3,4,5,6]
k = 2
print("Rotated Array: ",rotateArray(nums,k))