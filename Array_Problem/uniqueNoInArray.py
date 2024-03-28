def uniqueNo(array):
    res = []
    for num in array:
        if num not in res:
            res.append(num)
    return res
array = [1,2,2,3,3,4,5,5]
print("Uinque Number : ",uniqueNo(array))