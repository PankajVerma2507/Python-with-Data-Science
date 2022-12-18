A = {1,2,3,4,5}
B = {4,5,6,7,8}

# use |operator
#print(A|B)

#  use union function
#A.union(B)

print(B.union(A))

# Set difference
A = {1,2,3,4,5}
B = {4,5,6,7,8}
# use - operator on A
print(A-B)

print(A.difference)

print(B - A)
# set symmetric difference
A = {1,2,3,4,5}
B = {4,5,6,7,8}
# use ^ operator
print(A^B)

print(A.symmetric_difference(B))
