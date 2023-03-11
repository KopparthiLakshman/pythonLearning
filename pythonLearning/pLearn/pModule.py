
from random import shuffle, randint

# print("Lakshman")


if 1==12:
    for i in "man":
        print("No Of Iteration")
elif 1==1:
    pass
# else:
#     break


print(list(range(0,10,2)))



stringName = "python"

for index,value in enumerate(stringName):
    print(value)


mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','d','c']


for item in zip(mylist1, mylist2):
    print("Zipping elements in list :", item)


print ('x' in [1,2,3,4])
print (1 in [1,2,3,4])
print ('key' in {'key':12})
print (12 in {'key':12})

dic =  {'key':12}

print("verifying the values in the dictionary :", 12 in dic.values())
print('asdsa:', 'key' in dic.keys())



listshuffle = [1,2,3,4,5,6,7,8,9]
shuffle(listshuffle)
print(listshuffle)

myra = randint(0,100)
print(myra)

# num1 = input("prompt :")

# print(type(num1))


# ListComprehension

mylist3 = [x for x in 'LAKSHMAN']
mylist4 = [x for x in range(0, 12)]
mylist4 = [x*2 for x in range(0, 12)]
mylist5 = [x*2 for x in range(0, 12) if x%2!=0]

print(mylist5)

mylist6 = [x if x%2==0 else 'oddnum' for x in range(0,10)]

print(mylist6)


mylistInnerloop = [x*y for x in [1,2,3] for y in [10,10,10]]

print(mylistInnerloop)


