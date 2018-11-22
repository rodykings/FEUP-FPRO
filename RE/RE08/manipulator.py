# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:22:08 2018

@author: Rodrigo Reis
"""

#Insert integer e at position idx

final_result = ""
l = []

def print_f(l):
    global  final_result
    final_result += str(l) + " "

def manipulator(l, cmds):
    global final_result
    for i in cmds:
        a_list = i.split()
        if a_list[0] == "print":
            print_f(l)
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

print(manipulator([], ["insert 0 5", "insert 1 10", "insert 0 6","print", "remove 6", "append 9", "append 1", "sort", "print",
"pop", "reverse", "print"]))