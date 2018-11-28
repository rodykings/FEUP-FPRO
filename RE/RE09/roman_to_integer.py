def roman_to_integer(astring):
    
    dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
    result = 0
    intlist = []
    
    for i in astring:
        if i in dict:
            intlist.append(dict[i])    
     
    print(intlist)
    
    for i,value in enumerate(intlist):
        if i + 1 < len(intlist):
            if value >= intlist[i+1]:
                result += value
            else:
                result -= value
        else:
            result += value
            
    return result

print(roman_to_integer('LXXXIV'))
print(roman_to_integer("XLIII"))
print(roman_to_integer('MMMCMXCIX'))