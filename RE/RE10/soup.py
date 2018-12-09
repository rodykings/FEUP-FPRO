def recursion(matrix, word, alist):
       
    for il,line in enumerate (matrix):
            for ic,char in enumerate (line):
                    if char == word[0] and len(word)>1 :
                            hey =[matrix[il+i][ic+i]  for i in range(-1, 2, 1)]
                            if n == word[1]:
                                alist.append([il, ic])
                        
    return alist

def soup(matrix, word):
    
    collum_dict = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E"}
    
    alist = []
    recursion(matrix, word, alist)
    
    
    
mx = (('X', 'A', 'B', 'N', 'T', 'O'),
('Y', 'T', 'N', 'R', 'I', 'T'),
('U', 'P', 'O', 'M', 'D', 'S'),
('I', 'O', 'H', 'U', 'O', 'O'),
('R', 'T', 'E', 'L', 'Q', 'X'),
('I', 'W', 'J', 'K', 'P', 'Z'))

print(soup(mx, 'PORTO')) #returns the string "C2" (as illustrated above)
print(soup(mx, 'HOTEL')) #returns the string "D3"
print(soup(mx, 'RIO')) #returns the string "B4"