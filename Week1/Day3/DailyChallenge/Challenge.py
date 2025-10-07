# Step 1 : Créer la classe Farm
class Farm:
    # Step 2 : Implémenter la méthode __init__
    def __init__(self, farm_name):
        # Attribut du nom de la ferme
        self.name = farm_name
        # Dictionnaire pour stocker les animaux et leurs quantités
        self.animals = {}

    # Step 3 : Méthode add_animal
    def add_animal(self, animal_type, count=1):
        # Si l'animal existe déjà, on ajoute la quantité
        if animal_type in self.animals:
            self.animals[animal_type] += count
        # Sinon, on crée une nouvelle entrée
        else:
            self.animals[animal_type] = count

    # Step 4 : Méthode get_info
    def get_info(self):
        # Créer une liste de lignes de texte pour la mise en forme
        lines = [f"{self.name}'s farm", ""]

        # Parcourir les animaux triés par ordre alphabétique
        for animal in sorted(self.animals.keys()):
            lines.append(f"{animal} : {self.animals[animal]}")

        # Ajouter les lignes finales
        lines.append("")
        lines.append("    E-I-E-I-0!")

        # Retourner le texte final sous forme de chaîne
        return "\n".join(lines)

    # Step 6 : Méthode get_animal_types (Bonus)
    def get_animal_types(self):
        # Retourner la liste des animaux triée alphabétiquement
        return sorted(self.animals.keys())

    # Step 7 : Méthode get_short_info (Bonus)
    def get_short_info(self):
        # Récupérer les animaux triés
        types_sorted = self.get_animal_types()

        # Fonction pour mettre un "s" si la quantité est supérieure à 1
        def pluralize(name):
            return name + "s" if self.animals.get(name, 0) > 1 else name

        # Appliquer la pluralisation à chaque nom
        animals_list = [pluralize(a) for a in types_sorted]

        # Construire une phrase fluide selon le nombre d’animaux
        if not animals_list:
            joined = "no animals"
        elif len(animals_list) == 1:
            joined = animals_list[0]
        elif len(animals_list) == 2:
            joined = f"{animals_list[0]} and {animals_list[1]}"
        else:
            joined = f"{', '.join(animals_list[:-1])} and {animals_list[-1]}"

        # Retourner la phrase finale
        return f"{self.name}'s farm has {joined}."


# Step 5 : Tester le code de la ferme
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())

# Bonus : tester les méthodes supplémentaires
# print(macdonald.get_animal_types())   # ['cow', 'goat', 'sheep']
# print(macdonald.get_short_info())     # "McDonald's farm has cows, goats and sheeps."
