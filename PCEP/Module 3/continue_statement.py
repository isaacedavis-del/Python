user_word = input("Please enter a word: ")
user_word = user_word.upper()
vowels = {"A", "E", "I", "O", "U"}

for letter in user_word:
    if letter in vowels:
        continue
    print(letter)