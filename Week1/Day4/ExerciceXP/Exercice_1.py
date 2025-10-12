# Exercise 1: Pets

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around."


class Bengal(Cat):
    def sing(self, sounds):
        return f"{self.name} says {sounds}"


class Chartreux(Cat):
    def sing(self, sounds):
        return f"{self.name} says {sounds}"


# etape 1: Create the Siamese class (inherits from Cat)
class Siamese(Cat):
    def sing(self, sounds):
        return f"{self.name} says {sounds}"


# etape 2: Create a list of cat instances
bengal_cat = Bengal("Simba", 3)
chartreux_cat = Chartreux("Luna", 5)
siamese_cat = Siamese("Milo", 2)
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# etape 3: Create a Pets instance using the list
sara_pets = Pets(all_cats)

# etape 4: Take cats for a walk
sara_pets.walk()

# >> Simba is just walking around.
# >> Luna is just walking around.
# >> Milo is just walking around.