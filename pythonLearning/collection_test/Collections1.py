from collections import Counter
import os
import shutil
from test.test_decimal import file
from shutil import SameFileError


my_list = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6]
print(Counter(my_list))
c = Counter(my_list)
print(c.most_common())
print(c.values())
print(c.keys())

def Create_file():
    print(os.getcwd())
    path = os.getcwd()
    file_exists = os.path.exists(path+"\practicePython.txt")
    if(file_exists==False):
        f = open("practicePython.txt","w")
        f.write("This is a practice file")
        f.close
        
def move_file_into_another_dir(func):
    func()
    print(os.getcwd())
    print(os.listdir(os.getcwd()))
    try:
        shutil.move("practicePython.txt", 'C:\\Users\\DELL\\git\\repository\\pythonLearning\\pLearn')
    except:
        SameFileError
# Create_file()
move_file_into_another_dir(Create_file)
