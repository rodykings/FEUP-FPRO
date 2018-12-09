def calculator(expr):
    
    result = 0
    atuple = ()
    
    if type(expr) is not tuple:
        return expr
    
    for i in expr:
        if type(i) is tuple:
            atuple += (calculator(i),)
        else:
            atuple += (i,)
            if len(atuple) == 3:
                #add
                if atuple[1] == "+":
                    result += (atuple[0] + atuple[2])
                #sub
                elif atuple[1] == "-":
                    result += (atuple[0] - atuple[2])
                #mult    
                elif atuple[1] == "*":
                    result +=  (atuple[0] * atuple[2])
        
    return result
