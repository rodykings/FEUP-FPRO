 
def sort_by_field(filename, field):
    final_list = []
    final_str = ""
    first_line = []
    field_dict = {}
    
    with open(filename, "r") as my_file:
        first_line = my_file.readline().strip("\n").split(",")
        
        for k,f in enumerate(first_line):
            field_dict[f] = k
        
        my_list = "".join(my_file.readlines()).split("\n")
    for lines in my_list:
        final_list.append(lines.split(","))
        
    final_list = sorted(final_list, key=lambda x: x[field_dict[field]])
    
    final_str += ",".join(first_line) + "\n"
    for i in final_list:
        final_str += ",".join(i) + "\n"
    
    return final_str
