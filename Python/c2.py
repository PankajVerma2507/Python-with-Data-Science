class Cat:
    # constractor
    def _init_(self,name,age,bread):
        # syntax for instance_variable
        # self.<attribute> = <parameter>
        self.name = name
        self.age = age
        self.bread = bread

cat1 = Cat('soni',3, 'persian')
cat2 = Cat('mia', 2, 'Slamesa')
cat3 = Cat('Molly', 4, 'Egyptian Mau')

print(cat1.name, cat1.age, cat1.bread)
print(cat2.name, cat2.age, cat2.bread)
print(cat3.name, cat3.age, cat3.bread)