class Dog:
    bread = 'Labrador'
    age = 3
    name = 'Tommy'

# object instantation
dog1 = Dog()
dog1.name = 'Sheru'
dog1.age = 5
dog1.bread = 'German shepherd'

dog2 = Dog()
dog2.name = 'Rex'
dog2.age = 2
dog2.bread = 'Golden Retrieve'

dog3 = Dog()
dog3.name = 'Buddy'
dog3.age = 4
dog3.bread = 'Pug'

print(dog1.name,dog1.age,dog1.bread)
print(dog2.name,dog2.age,dog2.bread)
print(dog3.name,dog3.age,dog3.bread)