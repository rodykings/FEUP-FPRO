def greatest(num):
    list_nums = []
    
    while num > 0:
        list_nums.append(str(num % 10))
        num //= 10   
        
    return int("".join(sorted(list_nums, reverse = True)))

print(greatest(7187))

