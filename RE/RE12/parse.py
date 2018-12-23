def parse(filename):
    with open(filename, "r") as my_file:
        my_str =  [i.strip("\n ") for i in my_file.readlines()]
    
    final_str = ""
    
    for i in my_str:
        if i == "(":
            final_str += "("
        else:
            final_str += i + ","
            
    final_str = "("+final_str+")"
    
    return eval(final_str)
