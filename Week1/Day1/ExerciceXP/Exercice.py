# Exercise 1 : Hello World

from sys import last_value


print("Hello World, " * 4)

# Exercise 2 : Some Math

print((99**3) * 8)

# Exercise 3 : What’s your name ?

my_name = "Brian"

name = input("Please enter your name: ")
if name == my_name:
    print("Wow, we have the same name! You're as cool as me 😎")
else:
    print(f"You are not {my_name}, you are {name}")

# Exercise 4 : Tall enough to ride a roller coaster

height = int(input("Please enter your height in cm: "))
if height >= 145:
    print("You are tall enough to ride a roller coaster")
else:
    print("You are not tall enough to ride a roller coaster")

# Exercise 5 : Favorite Numbers

my_fav_numbers = set([10])

my_fav_numbers.add(20)
my_fav_numbers.add(30)

my_fav_numbers.remove(30)

friend_fav_numbers = set([50])

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 6: Tuple

my_tuple = (1, 2, 3, 4, 5)

# Les tuples sont immuables, donc on ne peut pas ajouter de nouveaux éléments

# Exercise 7: List Manipulation

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples")) 
basket.clear()
print(basket)

# Exercise 8 : Sandwich Orders

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich}")