while True:
    try:
        c0 = int(input("Please choose a non-negative and non-zero integer: "))
        if c0 > 0:
            break      
    except ValueError:
        print("The number you entered is not an integer, please try again.")      

steps = 0

while c0 != 1:
    c0 = int(c0 / 2) if c0 % 2 == 0 else int(3 * c0 +1)
    steps += 1
    print(c0)

print(f"steps = {steps}")