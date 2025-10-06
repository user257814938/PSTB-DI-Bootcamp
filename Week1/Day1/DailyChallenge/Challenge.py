# Challenge 1

number = int(input("Please enter a number: "))
length = int(input("Please enter a length: "))

multiples = [number * i for i in range(1, length + 1)]
print(multiples)

# Challenge 2

word = input("Enter a word: ")

new_word = word[0]

for letter in word[1:]:
    if letter != new_word[-1]:
        new_word += letter

print(new_word)