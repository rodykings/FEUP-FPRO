#1.sort_by_f
def sort_by_f(l):
    return sorted([i for i in l], key=lambda x:5-x if x>=5 else x)

