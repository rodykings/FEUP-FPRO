
#create result matrix
def matrix_result(lines, collumns):
    R = []
    line = []
    for i in range(0, collumns):
        line.append(0)
    for t in range(0, lines):
        R.append(line.copy())
    return R        
            
def mult(M, N):
    
    R = matrix_result(len(M), len(N[0]))
    
    if len(M[0]) == len(N):
        #ITERATE M ROWS
        for r_M in range(0, len(M)):
            #ITERATE N COLLUMNS
            for c_N in range(0, len(N[0])):
                #ITERATE N ROWS:
                for r_N in  range(0, len(M[0])):
                    R[r_M][c_N] += M[r_M][r_N] * N[r_N][c_N]
                    
        return R   
      
    else:
        return[]
        
print(mult([[1, 2], [3, 4]], [[2, 0], [1, 2]]))
print(mult([[1, 2, 3], [4, 5, 6]], [[9], [8], [7]]))