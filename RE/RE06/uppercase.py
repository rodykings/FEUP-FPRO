def uppercase(astring):
    
    for i in range(0,3):
        if astring[i].isupper() and astring[i].isalpha():
            break;
        else:
            return astring 
    return astring.upper()
