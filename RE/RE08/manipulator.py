
def manipulator(l, cmds):
    final_result = ""
    
    for i in cmds:
        a_list = i.split()
        if a_list[0] == "print":
            final_result += str(l) + " "
        elif a_list[0] == "insert":
            l.insert(int(a_list[1]), int(a_list[2]))
        elif a_list[0] == "remove":
            l.remove(int(a_list[1]))
        elif a_list[0] == "append":
            l.append(int(a_list[1]))
        elif a_list[0] == "sort":
            l.sort()
        elif a_list[0] == "pop":
            l.pop()
        elif a_list[0] == "reverse":
            l.reverse()
    return final_result    

    
print(manipulator([2, 4], ["print", "remove 4", "append 1", "sort",
"print", "pop", "reverse", "print"]))