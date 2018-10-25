def get_positions(word_list, sentence):
    
    final_str = "";
    for i in range(0, 2, 1):
        for n in range(0, 3, 1):
           if sentence.split(" ")[i] == word_list[n]:
                  final_str += str(n) + " "
          
    return final_str.split(" ")[0] + " " + final_str.split(" ")[1]

print(get_positions(["hello", "world", "lousy"], "lousy world"))
print(get_positions(["hello", "lousy", "world"], "lousy world"))
print(get_positions(["hello", "brave", "world"], "hello world"))
print(get_positions(["hello", "brave", "hello"], "hello hello"))
