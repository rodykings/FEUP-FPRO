
def isomorphic(astring1, astring2):
    
    dict = {}
    valueslist = []
    result = ()
    
    for i, values in enumerate(astring1):
        dict[values] = astring2[i]
    
        
    for i in dict.values():
        if i not in valueslist:
            valueslist.append(i)
            continue
        else:
            return "'{}' and '{}' are not isomorphic".format(astring1, astring2)
    
    for i in astring2:
        if i not in dict.values():
            return "'{}' and '{}' are not isomorphic".format(astring1, astring2)
            
    
    for key, value in dict.items():
        result += ((key, value),)
    
    return "'{}' and '{}' are isomorphic because we can map: {}".format(astring1, astring2, str(list(result)))

    
print(isomorphic('foo', 'bar'))
print(isomorphic('paper', 'title'))
print(isomorphic('ab', 'aa'))