

def local_minima(alist, n):

    final_tuple = ()
        
    neighbors = (n-1)//2 
    
    for (i, value) in enumerate(alist):
        #first in the list
        if i == 0:
            verify = True
            for t in range(1, n):
                if value > alist[t]:
                    verify = False   
                    break
            if verify == True:
                final_tuple += ((value, i),)
            
        #last in the list    
        elif i == len(alist)-1:
            verify = True
            for t in range(len(alist)-n, len(alist)-1, -1):
                if value > alist[t]:
                    verify = False
                    break
            if verify == True:
                final_tuple += ((value, i),)
        
        #if is in the middle     
        else:

            verify = True
            #neighborhood right
            if  i + neighbors >= len(alist)-1:  
                if i+1 == len(alist)-1:
                    if value > alist[i+neighbors]:
                        verify = False
                else:
                    for t in range(i+1, len(alist)-1):
                        if value > alist[t]:
                            verify = False   
                            break   
            else:
                if i+1 == i+neighbors:
                    if value > i+neighbors:
                        verify = False
                else:
                    for t in range(i+1, i+neighbors):
                        if value > alist[t]:
                            verify = False   
                            break
            
            #neightborhood left
            if  i - neighbors >= 0: 
                
                if i-1 == i-neighbors:
                    if value > alist[t]:
                        verify = False
                else:
                    for t in range(i-1, i-neighbors, -1):
                        if value > alist[t]:
                            verify = False   
                            break
            else:
                for t in range(i-1, 0, -1):
                    if value > alist[t]:
                        print(value)
                        verify = False   
                        break
               
    
            if verify == True:
                final_tuple += ((value, i),)
        
        #print(minimals)
        #print(index)
        #joining minimals and index
    
    return list(final_tuple)
       
print(local_minima([10, 3, 3, 14, 5, 7, 4], 3))
print(local_minima([0, 3, 3, 14, 5, 7, 4], 3))