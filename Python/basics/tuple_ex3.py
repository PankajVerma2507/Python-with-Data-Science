# tuple - set - list (interchangeable)

x = [1,2,3,4,5,6,6,7]
print(x)
xt = tuple(x) # list - > tuple
print(xt)
xl = list(xt) # tuple - > list
print(xl)
xs = set(x) # list -> set
print(xs)
xl = list(xs) #set -> list
print(xl)
xs = set(xt) # tuple -> set
print(xs)
xt = tuple(xs) # set -> tuple
print(xt)

# wap to crreate a tuple, by taking ten inputs from the user
x = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(x)