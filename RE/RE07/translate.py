
def translate(astring, table):
    new_string = ""

    for i in table:
        for t in astring:
            if i[0] == t:
                astring = astring.replace(t, str(i[1]))
                break
               
    return astring       

