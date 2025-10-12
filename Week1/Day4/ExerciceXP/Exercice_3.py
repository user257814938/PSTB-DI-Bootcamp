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