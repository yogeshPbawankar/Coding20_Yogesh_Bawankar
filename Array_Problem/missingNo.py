def missingNo(array):
    array = sorted(array)
    res = []
    for i in range(len(array) - 1):
        if array[i + 1] != array[i] + 1:
            return array[i] + 1

num = [7, 10, 2]
print("Missing no is:", missingNo(num))
