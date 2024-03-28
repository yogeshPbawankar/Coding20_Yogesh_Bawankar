def reverseArray(array):
    if len(array) == 1:
        return array
    st = 0
    end = len(array) - 1  
    mid = len(array) // 2  
    if len(array) % 2 == 0:
        # even array
        while st < mid:  
            array[st], array[end] = array[end], array[st]
            st += 1
            end -= 1
    else:# odd array
        while st != mid:  
            array[st], array[end] = array[end], array[st]
            st += 1
            end -= 1
    return array

list_input = []
n = int(input("Enter the size of array: "))
for i in range(n):
    list_input.append(int(input()))

print("OUTPUT REVERSE ARRAY: ", reverseArray(list_input))
