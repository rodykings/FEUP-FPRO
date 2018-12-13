#4.override
def override(l1, l2):
    return sorted([i for i in l2] + [i for i in l1 if (i[0] not in (t[0] for t in l2))], key= lambda x:x[0]) 
    