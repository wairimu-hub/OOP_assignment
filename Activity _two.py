# Base class
class Animal:
    def domesticated(self):
        pass  

# Subclasses showing different uses of being domesticated
class Cow(Animal):
    def domesticated(self):
        return "The cow is domesticated for milk and meat 🥛🥩"


class Chicken(Animal):
    def domesticated(self):
        return "The chicken is domesticated for eggs and meat 🍳🍗"


class Sheep(Animal):
    def domesticated(self):
        return "The sheep is domesticated for wool and meat 🧶🍖"


class Donkey(Animal):
    def domesticated(self):
        return "The donkey is domesticated for transport and farm work 🐴🌾"

animals = [Cow(), Chicken(), Sheep(), Donkey()]

#output
for a in animals:
    print(a.domesticated())
