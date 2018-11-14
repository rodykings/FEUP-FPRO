
def translate(astring, table):
    new_string = ""

    for i in table:
        for t in astring:
            if i[0] == t:
                astring = astring.replace(t, str(i[1]))
                break
               
    return astring       

print(translate("Hello World", (('a', 1), ('e', 2), ('i', 3),('o', 4), ('u', 5), ('!', ':'))))
print(translate("Testing this string...", ((' ', '--'), ('.','!'), ('i', 'o'), ('t', 'tt'))))