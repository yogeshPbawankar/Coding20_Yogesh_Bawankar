def reverseArray(nums):
    i , j = 0, 0 
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] < nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
"""
# Optimize Approch 
    return sorted(nums,reverse = True)
"""
array = [1,2,3,4,5]
print("Reverse Array: ",reverseArray(array))