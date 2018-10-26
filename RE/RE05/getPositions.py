def get_positions(word_list, sentence):
    
    if sentence == (word_list[0] + " " + word_list[1]) :
        return  "0 1"
    elif sentence == (word_list[0] + " " + word_list[2]):
        return  "0 2"
    elif sentence == (word_list[1] + " " + word_list[0]):
        return "1 0"
    elif sentence == (word_list[1] + " " + word_list[2]):
        return "1 2"
    elif sentence == (word_list[2] + " " + word_list[0]):
        return "2 0"  
    elif sentence == (word_list[2] + " " + word_list[1]):
        return "2 1"  

print(get_positions(["hello", "world", "lousy"], "lousy world"))
print(get_positions(["hello", "lousy", "world"], "lousy world"))
print(get_positions(["hello", "brave", "world"], "hello world"))
print(get_positions(["hello", "brave", "hello"], "hello hello"))
