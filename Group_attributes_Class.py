import random


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newAge):
        self.age = newAge
    def set_name(self, newName =""):
        self.name = newName
    def classification(self):
        return "Animal"
    def __str__(self):
        return self.classification()+": "+str(self.get_name())+":"+str(self.age)
    
class Cat(Animal):
    def speak(self):
        print("Meow")
    def classification(self):
        self.classification = "Cat"
    def __str__(self):
        return "Cat:"+str(self.name)+":"+str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def classification(self):
        return "Person"
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self,other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(f"{self.name} is {abs(diff)} years older than {other.name}")
        else:
            print(f"{other.name} is {abs(diff)} years younger than {self.name}")
    def __str__(self):
        return f"Person: {self.name}:{self.age}"
    
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()

        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need to sleep")
        else:
            print("I am watching TV")
    def __str__(self):
        return f"Student:{self.name}:{self.age}:{self.major}"

        

class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag +=1
    def classification(self):
        return "Rabbit"
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        return Rabbit(0, self, other)
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \
            and self.parent2.rid == other.parent2.rid
        parents_oposite = self.parent1.rid == other.parent2.rid \
            and self.parent2.rid == self.parent1.rid
        return parents_same or parents_oposite
peter = Rabbit(2)
peter.set_name("Peter")
hopsy = Rabbit(3)
hopsy.set_name("Hopsy")
mopsy = peter + hopsy
mopsy.set_name("Mopsy")
print(mopsy.get_parent1())