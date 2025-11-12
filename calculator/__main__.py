from add import sum
from subtract import subtraction


print("Select operation")
print("1. Addition")
print("2. Subtraction")

choice = input("Enter choice(1/2): ")
if choice == '1':
        sum()
elif choice == '2':
        subtraction()
else:
        print("Invalid input")

