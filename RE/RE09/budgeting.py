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
    
    final_wish = {}
    
    while tospend(wishlist, catalog) > budget:
        if wishlist[catalog[-1][0]] == 1:
            wishlist.pop(catalog[-1][0])
        else:
            wishlist[catalog[-1][0]] -= 1
    
    print(value)
#    while sum(catalog[1]) > budject
#    for product in catalog:
#        if budget >= product[1]:
#            budget -= product[1]
#            if product[0] in final_wish:
#                final_wish[product[0]] += 1
#            else:
#                final_wish[product[0]] = 1
#        else:
#            continue
#    
#    return final_wish

    
    
#    wishlisted = []
#    
#    for i in w:
#        wishlisted.append([i[0], i[1], products[i[0]]])
#    
#    sorted
#    print(wishlisted)
    
    
#    value = 0
#    for i in wishlisted:
#        if value + products[i[0]] <= budget:
#            value += products[i[0]]
#            continue
#        else:
#            i[1] -= 1
#            if i[1] == 0:
#                wishlisted.remove([i[0], i[1]])
   
#    return wishlisted


print(budgeting(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40,
'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))
 
    
print(budgeting(1500, {'xbox': 250, 'smartphone': 500, 'jeans': 50,
'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1,
'xbox':1}))
    
print(budgeting(750, {'nintendo': 100, 'mouse': 20, 'hoodie': 45, 'backpack': 30, 'tv': 300}, {'nintendo': 1, 'mouse': 1, 'hoodie': 4, 'tv': 2}))



    