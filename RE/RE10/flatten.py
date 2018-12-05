
def flatten(alist):
    
    final = []
    
    for i in alist:
        if type(i) is list:
            final += flatten(i)
        else:
            final.append(i) 
    return final    

print(flatten(['Hello', [2, [[], False]], [True]]))