def cut(filename, delimiter, field):
    finalstr = ""
    with open(filename, "r") as file:
            for line in file:
                line_list = line.split()
                if type(field) is list:
                    for i in tuple(field):
                        finalstr += str(line_list[i-1]) + ","
                    finalstr = finalstr[:-1]
                    finalstr += "\\n"
                else:
                    finalstr += str(line_list[field-1]) + '\\n'
    return finalstr[:-2]        
    
print(cut("data.csv", ",", 2))
print(cut("data.csv", ",", [2,4]))