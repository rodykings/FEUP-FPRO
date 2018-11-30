#sort rule
def sort_rule(alist):
    
    return alist[1]
    
def tospend(wishlist, catalog):
    value = 0
    for i in catalog:
        if i[0] in wishlist:
            value += wishlist[i[0]] * i[1]   
        else:
            continue
    return value
    
#budgeting
def budgeting(budget, products, wishlist):
    
    catalog = []
    
    for k,v in products.items():
        if k in wishlist:
            catalog.append([k,v])      

    catalog = sorted(catalog, key=sort_rule, reverse=True)
    
    while budget < tospend(wishlist, catalog):
        if wishlist[catalog[-1][0]] == 1:
            wishlist.pop(catalog[-1][0])
            catalog.pop()
        else:
            wishlist[catalog[-1][0]] -= 1
            
    return wishlist
