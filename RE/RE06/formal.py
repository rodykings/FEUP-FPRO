def formal(name):
    split_name = name.replace(" de ", " ")
    split_name = split_name.replace(" e ", " ")
    split_name = split_name.split()

    result = split_name[-1] + ", "
    for i in split_name[0:len(split_name)-1]:
       result += i[0].upper() + ". "
    
    return result