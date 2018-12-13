#5. reduce_map_filter
from functools import reduce

def reduce_map_filter(args):
        
    for i in args:
        if type(i) is tuple:
            return reduce_map_filter((args[0], args[1], reduce_map_filter(i)))
        
    if args[0]=="map":
        return list(map(args[1], args[2]))
    elif args[0]=="filter":
        return list(filter(args[1], args[2]))
    elif args[0]=="reduce":
        return int(reduce(args[1], args[2]))
        