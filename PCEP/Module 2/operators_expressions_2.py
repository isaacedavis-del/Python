while True:
    x = float(input("Enter value for x (non-zero): "))
    if abs(x) > 1e-10:
        break
    print("Error: x cannot be zero, please try again.")
while True:
    n = int(input("Enter a number of iterations n (positive integer): "))
    if abs(n) > 0:
        break
    print("Error: n must be a positive integer greater than 0, please try again.")
y = x

for _ in range(n-1):
    y = x + (1/y)

y = (1/y)
print("y =", y)