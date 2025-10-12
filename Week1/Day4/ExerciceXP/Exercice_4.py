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