a = 1, 2 , 3, 4 #type => tuple
print(a)
print(type(a))

x, y, *z =1, 2, 3, 4, 5
print(x, y,*z)
print(type(x),type(y),type(z))

# back to tuple
x = (23,24,25,)
y = tuple([3,2,1,5]) #converting a list to tuple

print(x,y)
print(type(x),type(y))