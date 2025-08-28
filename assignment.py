#Assignment 1 
# base class 
class Superhero:
    def __init__(self, name, power, suit, city, sidekick):
        self.name = name
        self.power = power
        self.suit = suit
        self.city = city
        self.sidekick = sidekick
    
    def call(self):
        print(f"{self.name} is here to protect {self.city} ")

# create a child class 
class EvilVillain(Superhero):
    def __init__(self, name, power, suit, city, sidekick, evil_plan):
        super().__init__(name, power, suit, city, sidekick)
        self.evil_plan = evil_plan

    # Polymorphism use the call method 
    def call(self):
        print(f"{self.name} is here to spread chaos with {self.evil_plan}")

# create objects 
hero = Superhero("BaseMan", "Mind Reading", "RedBlue", "Metrapolis", "Young")
villain = EvilVillain("DarkLord", "Darkness", "Black", "Gotham", "Shadow", "Take over the city")

# use methods 
hero.call()
villain.call()  

# Activity 2 
# Base class 
class Animal:
    def move(self):
        return "This animal moves somehow"

# Child classes with different implementations of move()
class Dog(Animal):
    def move(self):
        return "The dog runs on four legs"

class Bird(Animal):
    def move(self):
        return "The bird flies in the sky"

class Fish(Animal):
    def move(self):
        return "The fish swims in water"

class Snake(Animal):
    def move(self):
        return "The snake slithers on the ground"

# Polymorphism in action
#loop through each item in our list 
for animal in [Dog(), Bird(), Fish(), Snake()]:
    print(animal.move())

    

