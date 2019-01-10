
def exactly(s):
    counter = []
    for id, value in enumerate([i for i in s]):
        if value.isdigit():
            counter.append([id, value])
            
    
    return counter
print(exactly("acc?7??sss?3rr1??????5???5")) 

'''
returns the string:
    The sequence acc?7??sss?3rr1??????5???5 is OK with the pairs:
('73', '55')
   ''' 