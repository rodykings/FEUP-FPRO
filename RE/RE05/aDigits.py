def adigits(n1, n2, n3):
    
    n1_int = int(n1)
    n2_int = int(n2)
    n3_int = int(n3)
    
    #n1 
    if n1_int >= n2_int and n1_int >= n3_int:
        if n2_int > n3_int:
            return int(n1 + n2 + n3)
        else:
            return int(n1 + n3 + n2)
    
    #n2
    if n2_int >= n1_int and n2_int >= n3_int:
        if n1_int > n3_int:
            return int(n2 + n1 + n3)
        else:
            return int(n2 + n3 + n1)
            
    #n3
    if n3_int >= n1_int and n3_int >= n2_int:
        if n1_int > n2_int:
            return int(n3 + n1 + n2)
        else:
            return int(n3 + n2 + n1)
    

print(adigits("4", "2", "5"))
print(adigits("9", "1", "9"))
print(adigits("2", "2", "1"))
print(adigits("1", "2", "2"))
