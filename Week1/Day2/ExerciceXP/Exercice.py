# Exercise 1: Converting Lists into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

numbers = dict(zip(keys, values))
print(numbers)

# Exercise 2: Cinemax #2

family = {}
total_cost = 0

# Demander à l'utilisateur combien de membres ajouter
family_members = int(input("How many family members? "))

# Ajouter chaque membre manuellement
for i in range(family_members):
    name = input(f"Enter the name of member {i+1}: ")
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age

# Calcul du prix total
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name.capitalize()} has to pay ${price}")
    total_cost += price

print(f"Total cost for the family: ${total_cost}")

# Exercise 3: Zara

# 1) Création du dictionnaire 'brand' avec les données fournies

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_of_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 2) Modifier et accéder au dictionnaire

# a) Changer number_stores -> 2
brand["number_stores"] = 2

# b) Phrase décrivant les clients via type_of_clothes
clients = ", ".join(brand["type_of_clothes"])
print(f"Zara targets: {clients}.")  # ex: "Zara targets: men, women, children, home."

# c) Ajouter country_creation = "Spain"
brand["country_creation"] = "Spain"

# d) Si 'international_competitors' existe -> ajouter "Desigual"
if "international_competitors" in brand and isinstance(brand["international_competitors"], list):
    if "Desigual" not in brand["international_competitors"]:
        brand["international_competitors"].append("Desigual")

# e) Supprimer 'creation_date'
brand.pop("creation_date", None)

# f) Afficher le dernier élément de 'international_competitors'
if brand.get("international_competitors"):
    print("Last international competitor:", brand["international_competitors"][-1])

# g) Afficher les couleurs majeures aux US
print("Major colors in the US:", brand["major_color"]["US"])

# h) Nombre de clés du dictionnaire
print("Number of keys in brand:", len(brand))

# i) Afficher toutes les clés
print("All keys:", list(brand.keys()))

# 3) Bonus: fusion avec 'more_on_zara'
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000  # montrera l'écrasement de la valeur 2 -> 10000
}

brand.update(more_on_zara)
print("\nAfter merge with more_on_zara:")
print(brand)

# Exercise 4 : Some Geography

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

# Exemple 1 : avec deux paramètres
describe_city("Reykjavik", "Iceland")

# Exemple 2 : avec un seul paramètre (le pays reste par défaut)
describe_city("Paris")

# Exercise 5 : Random

import random

def compare_numbers(user_number):
    random_number = random.randint(1, 100)

    if user_number == random_number:
        print("Success! 🎉 The numbers match!")
    else:
        print(f"Fail! ❌ Your number: {user_number}, Random number: {random_number}")

compare_numbers(50)

# Exercise 6 : Let’s create some personalized shirts !

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")

make_shirt("large")                               
make_shirt("medium")                       
make_shirt("any size", "Custom message")      

make_shirt(size="extra large", text="Python is Awesome!")

# Exercise 7 : Temperature Advice

import random

def get_random_temp(season=None):
    if season == "winter":
        return random.uniform(-10, 16)
    elif season == "spring":
        return random.uniform(5, 25)
    elif season == "summer":
        return random.uniform(20, 40)
    elif season == "autumn":
        return random.uniform(0, 25)
    else:
        return random.uniform(-10, 40)

def main():
    month = int(input("Enter the current month number (1-12): "))

    if month in [12, 1, 2]:
        season = "winter"
    elif month in [3, 4, 5]:
        season = "spring"
    elif month in [6, 7, 8]:
        season = "summer"
    else:
        season = "autumn"

    temp = get_random_temp(season)
    print(f"The temperature right now is {temp:.1f}°C.")

    if temp < 0:
        print("Brrr, that’s freezing! 🥶 Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! ❄️ Don’t forget your coat.")
    elif 16 <= temp < 23:
        print("Nice weather 😎 — enjoy your day!")
    elif 23 <= temp < 32:
        print("A bit warm ☀️ Stay hydrated!")
    elif 32 <= temp < 40:
        print("It’s really hot 🔥 Stay cool and drink water.")

main()

# Exercise 8: Pizza Toppings

base_price = 10
topping_price = 2.5

toppings = []

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")

    if topping == "quit":
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

total_price = base_price + (len(toppings) * topping_price)

print("\nToppings:", ", ".join(toppings))
print(f"Total cost: ${total_price:.2f}")
