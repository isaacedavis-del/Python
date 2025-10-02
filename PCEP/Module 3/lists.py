hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

while True:
    try:
        middle_number = int(input("Please enter a new number for the middle of the list: "))
        break
    except ValueError:
        print("The new number must be an integer, please try again")

middle_index = int((len(hat_list) // 2))

hat_list[middle_index] = middle_number

hat_list = hat_list[:-1]


print(f"""The hat list is {hat_list} 
      It has length {len(hat_list)}""")