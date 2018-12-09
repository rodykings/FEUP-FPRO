def flatten(alist):
    
    final = []
    
    for i in alist:
        if type(i) is list:
            final += flatten(i)
        else:
            final.append(i) 
    return final    

def powerset(lst):
    
    result = [[]]
    
    for x in lst:
        result.extend([subset + [x] for subset in result])
        
    return sorted(result, key=lambda x:len(x))

def best_choice(bdg, dict, ps_wish):
    
    final_dict = {}
    bc = []
    cost = 0

    for i in ps_wish:
        price = 0
        for j in flatten(i):
            price += dict[j]
        if price <= bdg and price >= cost:
            cost = price
            bc = flatten(i)
     
    for i in bc:
        if i in final_dict:
            final_dict[i] += 1
        else:
            final_dict[i] = 1
        
    return final_dict


def budgeting2(budget, products, wishlist):
    
    wish_list = sorted([[k] for k,v in wishlist.items() for i in range(0, v)], key=lambda x:len(x))
    
    return best_choice(budget, products, powerset(wish_list))
