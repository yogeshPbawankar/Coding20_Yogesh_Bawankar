def fibonachi(x,y,n):
    i = 0
    res = []
    if n == 1:
        return x,y
    else:
        for i in range(2,n+1):
            c = x + y 
            x = y 
            y = c 
    return y
            
x = 0 
y = 1
n = int(input("Enter the stoping point: "))
print("Rquired fibonachi: ",fibonachi(x,y,n))