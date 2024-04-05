def removingHash(line):
    count = 0 
    res = ""
    for word in line : 
        if word == "#":
            count += 1 
    i = 0 
    
    while i < count:
        res += '#'
        i += 1 
        
    line = line.split("#")
    for word in line:
        res += word
        
    return res



line = "move#hash#to#front"
print("Hash was moved into first: ",removingHash(line))