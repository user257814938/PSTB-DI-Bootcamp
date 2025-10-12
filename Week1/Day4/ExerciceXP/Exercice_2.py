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