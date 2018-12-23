def cut(filename, delimiter, field):
    
    with open(filename, "r") as my_file:
        wtab_list = [i.strip("\n").split(delimiter) for i in my_file.readlines()]
    
    final_str = ""  
    
    if type(field) is list:
        for i in range(0, len(wtab_list)):
            for n in field:
                final_str += wtab_list[i][n-1] + delimiter
            final_str = final_str.strip(delimiter) + "\n"
        
    else:
        for i in wtab_list:
            final_str += i[field-1] + "\n"
            
    return final_str