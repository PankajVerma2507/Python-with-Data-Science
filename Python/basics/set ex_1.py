# # set cannot have duplicates
# # output: {1, 2, 3, 4}
# my_set = {1,2,3,4,3,2}
# print(my_set)

# # we can make set from a list
# # output: {1,2,3}
# my_set = set([1,2,3,2])
# print(my_set)
# my_set = {1,2,[3,4]}
# print(my_set)

# # initilize my_set
# my_set =[1,3]
# print(my_set)

# # add an element
# # output: {1,2,3}
# my_set.add(2)
# print(my_set)

# # add multiple elements
# my_set.update([2,3,4])
# print(my_set)

# #add list and set
# my_set.update([4,5],{1,6,8})
# print(my_set)

# initialize my_set
my_set = {1,3,4,5,6}
print(my_set)

# discard an elements
my_set.discard(4)
print(my_set)

# remove an element
# output:{1,3,5}
my_set.remove(6)
print(my_set)

# pop a random item
my_set.pop()
print(my_set)

# clear my_set
my_set.clear()
print(my_set)
