a = float(input("Enter the first number:"))

while True:
    b = float(input("Enter the second number (non-zero):"))
    if abs(b) > 1e-10:
        break
    print("Error: The second number cannot be zero. Please enter a non-zero number")

print(f"Addition: {a+b}")
print(f"Subtraction: {a-b}")
print(f"Multiplication: {round(a*b,2)}")
print(f"Division: {round(a/b,2)}")

print("\nThat's all, folks!")