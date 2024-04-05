def repeateFrontBackWord(line):
    f3 = line[:3]
    l3 = line[-3:]
    n = len(line)
    i = ""
    while len(i) < n: 
        i += l3
        i += f3
    return i
        
line = "Python"
print("Required O/P : ",repeateFrontBackWord(line))