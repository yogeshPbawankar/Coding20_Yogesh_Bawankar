def sortingArray(nums):
    n = len(nums)
    mid = n // 2
    i ,j =0,0
    # Accending order
    for i in range(mid):
        for j in range(mid -1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

    # Decending order
    for i in range(mid+1,n):
        for j in range(mid,n-1):
            if nums[j] < nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

    return nums

        
        
num = [1,3,4,5,6,9,8,7]
print("Result: ",sortingArray(num))