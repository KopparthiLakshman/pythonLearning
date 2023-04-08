from collections import Counter

my_list = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6]
print(Counter(my_list))
c = Counter(my_list)
print(c.most_common())
print(c.values())
print(c.keys())



