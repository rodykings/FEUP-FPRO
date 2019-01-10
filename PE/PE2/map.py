def map(pos, steps):
    pos_list = list(pos)
    steps_list = steps.split("-")
    
    for i in steps_list:
        if i == "up":
            pos_list[1] += 1
        elif i == "down":
            pos_list[1] -= 1
        elif i == "left":
            pos_list[0] -= 1
        elif i == "right":
            pos_list[0] += 1
        
    return tuple(pos_list)

print(map((0,0), "up-up-left-right-up-up"))