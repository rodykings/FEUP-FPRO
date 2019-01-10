
def interleave(alist1, alist2):
    if alist1 == [] or alist2 == []:
        return []
    else:
        return flatten([[flatten(alist1)[i],flatten(alist2)[i]]  for i in range(max(len(alist1)+1, len(alist2)+1))])
            
        
def flatten(alist):
    final = []
    
    for i in alist:
        if type(i) is list:
            final += flatten(i)
        else:
            final.append(i) 
    return final    

    
print(interleave([1, [4,2]], [3, [7,4]]))# returns the list [1,3,4,7,2,4]