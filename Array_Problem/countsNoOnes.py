def count(mat):
    max_count = 0
    max_idx = -1
    i,j =0,0
    for i in range(len(mat)):
        count = 0 
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                count += 1
        if count > max_count:
            max_count = count 
            max_idx = i
                    
    return [max_idx,max_count]

"""
# Another approch to solve this problem enumerate function will do ...

def count(mat):
    min_index = [0,0]
    def count(mat):
    min_index = [0,0]
    max_count = 0
    for i,val in enumerate(mat):
        count = val.count(1)
        if count>max_count:
            max_count = count
            min_index = [i,count]    
    return min_index   

"""       

mat = [[0,0],[1,1],[0,0]]
m = len(mat[0])
n = len(mat)
print(count(mat))