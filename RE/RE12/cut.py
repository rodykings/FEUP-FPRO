def cut(filename, delimiter, field):
    finalstr = ""
    with open(filename, "r") as file:
            for line in file:
                line_list = line.split()
                if type(field) is list:
                    for i in field:
                        finalstr += str(line_list[i-1]) + delimiter
                    finalstr += "\n"
                    finalstr.strip(delimiter)
                else:
                    finalstr += str(line_list[field-1]) + '\n'
    return finalstr       
    
print()