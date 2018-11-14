def find_dtype(atuple, data_type):

    final_tuple = ()
    for i in atuple:
        if type(i).__name__ == data_type:
            final_tuple += (i,)
    
    return final_tuple

print(find_dtype((1, False, "hello", 2., "world"), "str"))
print(find_dtype((1, 2, 3), "float"))
