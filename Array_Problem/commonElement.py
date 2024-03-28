def commonElement(num1,num2):
    num1= sorted(num1)
    num2 = sorted(num2)
    i = 0 
    j = 0
    res = []
    m = len(num1) -1
    n = len(num2) -1
    while i < m or j < n:
        if num1[i] == num2[j]:
            res.append(num2[j])
            j += 1
        else: 
            i += 1
    return res

    
num1 = [1,2,3,4,5]
num2 = [2,3,4,5,7]
print("Common Element In Array: ", commonElement(num1,num2))