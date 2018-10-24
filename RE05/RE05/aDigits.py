def adigits(num_1, num_2, num_3):
    
    n1 = int(num_1)
    n2 = int(num_2)
    n3 = int(num_3)
    final_str = ""
    
    #equal numbers
    if n1 == n2 and n2 == n3:
        return num_1 + num_2 + num_3
    
    #two iquals
    if n1 == n2:
        if n1 > n3:
            return num_1 + num_2 + num_3
        else:
            return num_3 + num_2 + num_1
    if n1 == n3:
        if n1 > n2:
            return num_1 + num_3 + num_2
        else:
            return num_2 + num_3 + num_1
    if n2 == n3:
        if n2 > n1:
            return num_2 + num_3 + num_1
        else:
            return num_1 + num_2 + num_3


    #n1 is the max number
    if n1 > n2 and n1 > n3:
        final_str += num_1
        if n2 > n3:
            final_str += num_2 + num_3
            return final_str
        elif n3 > n2:
            final_str += num_3 + num_2
            return final_str
        else:
            final_str += num_2 + num_3
            return final_str

    #n2 is the max number
    if n2 > n1 and n2 > n3:
        final_str += num_2
        if n1 > n3:
            final_str += num_1 + num_3
            return final_str
        elif n3 > n1:
            final_str += num_3 + num_1
            return final_str
        else:
            final_str += num_1 + num_3
            return final_str

    #n3 is the max number
    if n3 > n1 and n3 > n2:
        final_str += num_3
        if n1 > n2:
            final_str += num_1 + num_2
            return final_str
        elif n2 > n1:
            final_str += num_2 + num_1
            return final_str
        else:
            final_str += num_1 + num_2
            return final_str

print(adigits("4", "2", "5"))
print(adigits("9", "1", "9"))
