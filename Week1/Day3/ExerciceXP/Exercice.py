# Exercise 1: Cats

# Définition de la classe Cat
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Créer trois objets de type Cat
cat1 = Cat("Milo", 5)
cat2 = Cat("Luna", 3)
cat3 = Cat("Simba", 7)

# Step 2: Créer une fonction pour trouver le chat le plus âgé
def find_oldest_cat(cat1, cat2, cat3):
    oldest = max([cat1, cat2, cat3], key=lambda cat: cat.age)
    return oldest

# Step 3: Afficher les détails du chat le plus âgé
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

# Exercise 2 : Dogs

# Step 1: Créer la classe Dog
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Créer les objets davids_dog et sarahs_dog
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# Step 3: Afficher les détails et appeler les méthodes
print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Comparer les tailles des chiens
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same size!")

# Exercise 3 : Who’s the song producer?

# Step 1: Créer la classe Song
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Appeler la méthode pour chanter la chanson
stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo

# Step 1: Définir la classe Zoo
class Zoo:
    def __init__(self, zoo_name):
        # Nom du zoo
        self.zoo_name = zoo_name
        # Liste vide pour stocker les animaux
        self.animals = []

    # Ajouter un nouvel animal au zoo
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    # Afficher tous les animaux présents dans le zoo
    def get_animals(self):
        print("Animaux dans le zoo :", self.animals)

    # Vendre (supprimer) un animal du zoo
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    # Trier et grouper les animaux par première lettre
    def sort_animals(self):
        # Trier alphabétiquement
        self.animals.sort()
        grouped = {}

        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = [animal]
            else:
                grouped[first_letter].append(animal)

        # Sauvegarder le regroupement dans un attribut pour pouvoir le réutiliser
        self.grouped_animals = grouped
        return grouped

    # Afficher les groupes d’animaux
    def get_groups(self):
        for letter, group in self.grouped_animals.items():
            print(f"{letter}: {group}")

# Step 2: Créer une instance du zoo
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Utiliser les méthodes de la classe Zoo
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")

# Afficher la liste initiale
brooklyn_safari.get_animals()

# Vendre un animal
brooklyn_safari.sell_animal("Bear")

# Afficher la nouvelle liste
brooklyn_safari.get_animals()

# Trier et grouper les animaux
brooklyn_safari.sort_animals()

# Afficher les groupes
brooklyn_safari.get_groups()
