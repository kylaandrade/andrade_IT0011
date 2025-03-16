def divide(a, b):
    if b == 0:
        print("Division by zero is not allowed. Please try again.")
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Division by zero is not allowed. Please try again.")
        return None
    return a % b

def summation(a, b):
    if a > b:
        print("The second number must be greater than the first number. Please try again.")
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("------------------------------")
        print("Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[X] - Exit")
        print("------------------------------")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'X':
            print("Exiting the program...")
            break

        if choice in ['D', 'E', 'R', 'F']:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Please enter valid integers.")
                continue

            if choice == 'D':
                result = divide(num1, num2)
            elif choice == 'E':
                result = exponentiation(num1, num2)
            elif choice == 'R':
                result = remainder(num1, num2)
            elif choice == 'F':
                result = summation(num1, num2)

            if result is not None:
                print("Result:", result)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
