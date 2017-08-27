#Animal is an Object
class Animal(object):
    pass
#Dog is an Animal
class Dog(Animal):
    def __init__(self,name):
        #Dog HAS-A Name
        self.name = name
#cat is an Animal
class Cat(Animal):
    def __init__(self,name):
        #Cat Has-A Name
        self.name = name
#person is a object
class Person(object):
    def __init__(self,name):
        #person Has-A Name
        self.name = name
        #Person has a pet of somekind
        self.pet = None
#Employee is a person
class Employee(Person):
    def __init__(self, name, salary):
        #
        super(Employee,self).__init__(name)
        #Employee has a salary 
        self.salary = salary
#class Fish is a object
class Fish(object):
    pass
#Salmon is a fish
class Salmon(Fish):
     pass
#Halibut is a fish
class Halibut(Fish):
    pass
#rover is a dog
rover = Dog("Rover")
#satan is a cat
satan = Cat("Satan")
#mary is a person
mary = Person("mary")
#mary has a pet which is satan
mary.pet=satan
#Frank is a Employee whose salary 120000
frank = Employee("Frank",120000)
#frank has a pet which is rover
frank.pet=rover
flipper = Fish()
course = Salmon()
harry = Halibut()
