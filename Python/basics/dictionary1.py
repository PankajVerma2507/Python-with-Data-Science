# dictionary with integer key
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)

val =['Rajendra singh',30,10,'Accounts','Staff officer',60000,7]

val_dict ={
    'Employee': 'Rajendra Singh','Age': 30,
    'Experience': 10, 'Dept': 'Accounts',
    'Designation': 'Staff Officer', 'salary': 60000,
    'Team_size':7
}
# display a dict
print(val_dict)

# retrieval of value
ans = val_dict['Designation']# key in squiare brackets
print(ans)
print(val_dict['salary'])# Correct

# adding a data inside dict
val_dict['Company']='Acme.inc'

print(val_dict)
from pprint import pp, pprint
pp(val_dict)

