def sparse_dot_product(dict1, dict2):
    
    result = 0
    
    if dict1 == {} or dict2 == {}:
        return result
    
    for i in dict1.keys():
        if i in dict2:
            result += dict1[i] * dict2[i]
    return result

print(sparse_dot_product({0: 1, 1: 1}, {2: 1, 3: 1}))