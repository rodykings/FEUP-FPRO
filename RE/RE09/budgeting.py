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
            
    return tospend(wishlist, catalog)
    

print(budgeting(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40,
'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))
 
    
print(budgeting(1500, {'xbox': 250, 'smartphone': 500, 'jeans': 50,
'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1,
'xbox':1}))
    
print(budgeting(750, {'nintendo': 100, 'mouse': 20, 'hoodie': 45, 'backpack': 30, 'tv': 300}, {'nintendo': 1, 'mouse': 1, 'hoodie': 4, 'tv': 2}))



    