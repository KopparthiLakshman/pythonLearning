'''
Created on 11-Mar-2023

@author: DELL
'''


s = "split the string in to even and odd attending interview in may fot Masters"


for i in s.split():
#     if len(i)%2==0:
#         print(i, " : even")
#     else:
#         print(i,' : odd')
    if i[0] =='s':
        print(i)    
      
      
li = [c for c in range(0,11) if c%2==0]         
print([c for c in range(0,11) if c%2==0])