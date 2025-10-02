while True:
    try:
        year = int(input("Enter a year: "))
        if year >= 1582:
            break
        print("Not within the Gregorian calendar period, please try again.")
    except ValueError:
        print("The year must be an integer, please try again.")

if (year % 4 != 0) or (year % 100 == 0 and year % 400!=0):
    print("Common year")
else:
    print("Leap year")