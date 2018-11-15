def find_dtype(atuple, data_type):

    final_tuple = ()
    for i in atuple:
        if type(i).__name__ == data_type:
            final_tuple += (i,)
    
    return final_tuple


