'''
Created on 11-Mar-2023

@author: DELL
'''
from test.test_importlib.import_.test_fromlist import ReturnValue


def name_of_the_function(num1, num2):
    
    ''' comments to add in python file'''
    print("My First funtion in python")
    print(f' Print {num1} , {num2}')
    
    return num1+num2;
    


returvalue = name_of_the_function(1,2)

print(returvalue)