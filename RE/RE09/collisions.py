

def collisions(alist):
    
    
    intlist = []
    newlist = []
    sumlist = []
    dic = {}
    
    for i in alist:
        while i > 0:
            intlist.append(i % 10)
            i //= 10
        newlist.append(intlist)
        intlist = []

    for i in newlist:
        sumlist.append(sum(i) % 8)
    
    sumlist.sort()
    
    for i in sumlist:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
        
    return dic
    
