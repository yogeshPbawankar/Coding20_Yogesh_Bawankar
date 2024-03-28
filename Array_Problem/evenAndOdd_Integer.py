def even_Odd_Integer(array):
    even , odd = 1,1
    for num in array:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd
num = [1,2,3,4,5,6,7]
even , odd = even_Odd_Integer(num)
print(f"Even Count: {even} , Odd Count : {odd}")