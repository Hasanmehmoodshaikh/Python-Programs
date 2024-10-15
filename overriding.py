import abc 
from abc import ABC, abstractmethod

class Animal (ABC):
    def makesound(self):
        pass

class Dog(Animal):
    def makesound(self):
        print("bow wow")

class Cat(Animal):
    def makesound(self):
        print("meow meow")

class Goat(Animal):
    def makesound(self):
        print("Bay Bay")

c = Cat()
c.makesound()

d = Dog()
d.makesound()

g = Goat()
g.makesound()