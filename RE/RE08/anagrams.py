
def sort_rule(f):
    return (f[0].lower())

def anagrams(alist):
    
    alist_no_gaps = []
    index_list = []
    final_list = []
    no_anagrams = []
    
    if alist == []:
        return []
    
    
    for (idx, exp) in enumerate(alist):
            lower = exp.lower()
            alist_no_gaps.append("".join(sorted("".join(lower.split()))))
    
    
    same_index = []   
    for i in range(len(alist_no_gaps)):
        same_index.append(i)
        for t in range(i+1, len(alist_no_gaps)):
            if alist_no_gaps[i] == alist_no_gaps[t]:
                same_index.append(t)     
        if len(same_index) > 1:
            index_list.append(same_index)
        else:
            no_anagrams.append(i)
        same_index = []        
      
    print(index_list)
    
    sub_final = []
    for i, value_i in enumerate(index_list):
        for t, value_t in enumerate(value_i):
           sub_final.append(alist[index_list[i][t]]) 
        final_list.append(sorted(sub_final))
        sub_final = []
    
   
    final_list.append([alist[no_anagrams[0]]])
    
    final_list_sorted = sorted(final_list, key=sort_rule) 
    
    final_sorted = []
    for i in range(0, len(final_list_sorted)):
            if final_list_sorted[i][0] == final_list_sorted[i-1][0]:
                continue
            else:
                final_sorted.append(final_list_sorted[i])         
        
    return final_sorted
          
    