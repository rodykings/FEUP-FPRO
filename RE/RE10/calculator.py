
def calculator(expr):
    
    result = 0
    cal = ()
    
    for i in expr:
        if type(i) is tuple:
            cal += (calculator(i),)
        else:
            cal += (i,)
            if len(cal) == 3:
                #add
                if i == "+":
                    result += (expr[0] + expr[2])
                #sub
                elif i == "-":
                    result += (expr[0] - expr[2])
                #mult    
                elif i == "*":
                    result +=  (expr[0] * expr[2])
        
    return result
            
print(calculator(((1, '+', 2), '*', 3)))