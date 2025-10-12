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

# Exercise 2: Dogs

# etape 1: Define the Dog class
class Dog:
    def __init__(self, name, age, weight):
        self.name = name           # nom du chien
        self.age = age             # âge du chien
        self.weight = weight       # poids du chien

    def bark(self):
        # méthode pour faire aboyer le chien
        return f"{self.name} is barking"

    def run_speed(self):
        # calcule la vitesse de course : poids / âge * 10
        return self.weight / self.age * 10

    def fight(self, other_dog):
        # calcule la "puissance" des deux chiens
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        # compare et détermine le vainqueur
        if my_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}"
        elif my_power < other_power:
            return f"{other_dog.name} won the fight against {self.name}"
        else:
            return f"The fight between {self.name} and {other_dog.name} ended in a draw"


# etape 2: Create dog instances
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Max", 8, 15)

# etape 3: Test methods
print(dog1.bark())
# >> Rex is barking

print(dog2.run_speed())
# >> 83.33

print(dog1.fight(dog2))
# >> Buddy won the fight against Rex

# Exercise 3: Dogs Domesticated

# etape 1: Import the Dog class
# (ici on suppose que la classe Dog vient de l'exercice précédent)
from random import choice


class Dog:
    def __init__(self, name, age, weight):
        self.name = name           # nom du chien
        self.age = age             # âge du chien
        self.weight = weight       # poids du chien

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}"
        elif my_power < other_power:
            return f"{other_dog.name} won the fight against {self.name}"
        else:
            return f"The fight between {self.name} and {other_dog.name} ended in a draw"


# etape 2: Create the PetDog class that inherits from Dog
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)  # appel du constructeur de Dog
        self.trained = False                 # par défaut le chien n’est pas entraîné

    def train(self):
        # le chien aboie et devient entraîné
        print(self.bark())
        self.trained = True

    def play(self, *args):
        # affiche le nom de tous les chiens qui jouent ensemble
        dog_names = ", ".join(args)
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        # si le chien est entraîné, il fait un tour choisi au hasard
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet!")


# etape 3: Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
# >> Fido is barking

my_dog.play("Buddy", "Max")
# >> Fido, Buddy, Max all play together

my_dog.do_a_trick()
# >> Fido shakes your hand   (ou autre trick aléatoire)

# Exercise 4: Family and Person Classes

# etape 1: Define the Person class
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name   # prénom
        self.age = age                 # âge
        self.last_name = ""            # nom de famille vide par défaut

    def is_18(self):
        # renvoie True si la personne a 18 ans ou plus, sinon False
        return self.age >= 18


# etape 2: Define the Family class
class Family:
    def __init__(self, last_name):
        self.last_name = last_name     # nom de famille commun
        self.members = []              # liste des membres (Person objects)

    def born(self, first_name, age):
        # crée une nouvelle personne et l’ajoute à la famille
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name     # assigne le nom de famille
        self.members.append(new_person)           # ajoute à la liste des membres
        print(f"A new family member is born: {first_name} {self.last_name}, {age} years old.")

    def check_majority(self, first_name):
        # cherche la personne dans la famille par prénom
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():  # vérifie la majorité
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No family member found with the name {first_name}.")

    def family_presentation(self):
        # affiche le nom de la famille et la liste des membres
        print(f"\nThe {self.last_name} family:")
        for member in self.members:
            print(f"- {member.first_name} {member.last_name}, {member.age} years old.")
