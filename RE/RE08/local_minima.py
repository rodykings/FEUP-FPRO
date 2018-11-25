
def local_minima(alist, n):
    n = (n//2)
    result = []
    last_value = -20
    last_i = -20
    
    for i in range(len(alist)):
        current = alist[i]
        if (i-n) < 0:                                          
            another_list = alist[i:i+n+1]
            if min(another_list) == current:                      
                result.append((current, i))
                last_value = current
                last_i = i
        else:
            another_list = alist[i-n:i+n+1]                         
            if min(another_list) == current:
                if last_value == current and last_i == i-1:
                    last_value = current
                    last_i = i
                    pass
                else:
                    result.append((current, i))
                    last_value = current
                    last_i = i
    
    return result