
def unique(atuple):
    
   final_tuple = ()

   for i in atuple:
       if i not in final_tuple:
           final_tuple += (i,)    

   return tuple(sorted(final_tuple))


