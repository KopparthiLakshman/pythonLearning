import string
from pickletools import string1

print("Hello")
print('Hello')

Str = "lakshman"
Str = "new String"

print(Str)

input_from_Conosle = "Sample Text"
# input_from_Conosle = input("Enter from Console will be always string ")
print(input_from_Conosle)

a,b,c = 1,2,3

print(a , b,  c)

print(F'print the {a}')
print("Print the variable data a : {}".format(input_from_Conosle))

print(type(a))

print(isinstance(a, int))

tuple_object = (10,3)

print(type(tuple_object), " tuple unpacking " , tuple_object[0])

dict_obj = {"x":10, 'y':20}

print("value of X ion dict : ",dict_obj["x"])

print(type(dict_obj))

def loop_for(var1="Yes"):
    for i in range(0,2):
        print(i)
    
    for j in tuple_object:
        print(j)

    while True:
#         var1 = input("Enter value as Yes : ")
        if var1=="Yes":
            print("Exit from the loop")
            break
        else:
            continue
            
loop_for()

inputString = "sun raises in the east"
inputString = inputString.capitalize()
print(inputString)
print(inputString.istitle())
inputString = inputString.title()
print(inputString.title())
print(inputString.istitle())
