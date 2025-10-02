secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    try:
        guess = int(input("Secret number: "))
        if guess == secret_number:
            print("Well done, muggle! You are free now.")
            break
        else:
            print("Ha ha! You're stuck in my loop!")
    except ValueError:
        print("The secret number is an integer, please try again?")