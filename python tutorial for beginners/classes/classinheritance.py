class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):

        print("annoying")

#creating cat and dog objects




dog1=Dog()
dog1.bark()