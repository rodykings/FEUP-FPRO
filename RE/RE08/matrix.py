#     2 0
#     1 2
# 1 2|
# 3 4|

def matrix(M, N):

    R = []
    
    for i in 
    
    if len(M[0]) == len(N[0]):
        #ITERATE M ROWS
        for r_M in range(len(M)):
            #ITERATE N COLLUMNS
            for c_N in range(len(N[0])):
                #ITERATE N ROWS:
                for r_N in range(len(N)):
                    R[r_M][c_N] += M[r_M][c_N] * N[r_N][c_N]
        for r in R:
            print(r)
      
    else:
        return[]

matrix([[1, 2], [3, 4]], [[2, 0], [1, 2]])