# Demander à l'utilisateur d'entrer un mot
word = input("Entrez un mot : ")

# Créer un dictionnaire vide
letter_indexes = {}

# Parcourir chaque lettre avec son index
for index, letter in enumerate(word):
    # Si la lettre n'est pas encore dans le dictionnaire, l'ajouter avec une nouvelle liste
    if letter not in letter_indexes:
        letter_indexes[letter] = [index]
    # Si elle existe déjà, ajouter le nouvel index à la liste correspondante
    else:
        letter_indexes[letter].append(index)

# Afficher le dictionnaire final
print(letter_indexes)
