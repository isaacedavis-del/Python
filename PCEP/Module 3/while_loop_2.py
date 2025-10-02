while True:
    try:
        blocks = int(input("Enter the number of blocks: "))
        if blocks <0:
            print("Please enter a non-negative integer")
            continue
        break
    except ValueError:
        print("The number of blocks must be an integer please try again")
        
height = 0
next_row = 1

while blocks >= next_row:
    blocks -= next_row
    height += 1
    next_row += 1

print("The height of the pyramid:", height)