beatles = []
print("Step 1:", beatles)

beatles.extend(("John Lennon","Paul McCartney", "George Harrison"))
print("Step 2:", beatles)

other_beatles = ("Stu Sutcliff", "Pete Best")
for _ in range(len(other_beatles)):
    while True:
        beatle = input("Please type in the name of another beatle: ")
        if beatle in other_beatles:
            beatles.append(beatle)
            break
print("Step 3:", beatles)

del beatles[3:]
print("Step 4:", beatles)

beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))