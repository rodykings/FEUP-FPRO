# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:35:42 2018

@author: rodri
"""

#collisions([24, 42]) returns the dictionary: {6: 2} (because the hash 6 was
#found twice)
#collisions([1, 789, 100, 9807, 1208, 92, 101]) returns the dictionary:
#{1: 2, 0: 2, 3: 2, 2: 1}


def collisions(alist):
    
    
    intlist = []
    newlist = []
    sumlist = []
    dic = {}
    
    for i in alist:
        while i > 0:
            intlist.append(i % 10)
            i //= 10
        newlist.append(intlist)
        intlist = []
            
    
        
    for i in newlist:
        sumlist.append(sum(i) % 8)
    
    sumlist.sort()
    
    
    for i in sumlist:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
        
    return dic
    
    
    
print(collisions([1, 789, 100, 9807, 1208, 92, 101]))