import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    sys.exit(1) # finaliza o processo sem erro no programa

print(f"{x}/{y} = {result}")