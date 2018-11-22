#     2 0
#     1 2
# 1 2|
# 3 4|


R = []

#create result matrix
def matrix_result(lines, collumns):
    line = []
    for i in range(collumns):
        for t in range(lines):
            line.append(0)
        R.append(line)
        line = []        
            
def matrix(M, N):
    
    matrix_result(len(M), len(N[0]))
    
    if len(M) == len(N[0]):
        #ITERATE M ROWS
        for r_M in range(len(M)):
            #ITERATE N COLLUMNS
            for c_N in range(len(N[0])):
                #ITERATE N ROWS:
                for r_N in  range(len(M[0])):
                    R[r_M][c_N] += M[r_M][r_N] * N[r_N][c_N]
                    
        return R   
      
    else:
        return[]

print(matrix([[1, 2], [3, 4]], [[2, 0], [1, 2]]))