def unique(atuple):
    
   final_tuple = ()

   for i in atuple:
       if i not in final_tuple:
           final_tuple += (i,)    

   return tuple(sorted(final_tuple))

print(unique((8, 8, 1, 3, 1, 3, 5))) 
print(unique((1, 1 , 1 , 1)))
