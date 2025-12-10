import logo
print(logo.logo)
def calculator(n1, n2, operation):
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1 * n2
    elif operation == "/":
        return n1 / n2
    else:
        return "Invalid operation"

def user_same_calculator(result):
    choice = "yes"
    while choice == "yes":
        print(f"\nCurrent result: {result}")
        num2 = float(input("Enter next number: "))
        operation = input("Enter operation (+, -, *, /): ")

        result = calculator(result, num2, operation)
        print(f"New result: {result}")

        choice = input("Do you want to perform another calculation? (yes/no): ").lower()
    return result


# first calculation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

result = calculator(num1, num2, op)
print(f"Result: {result}")

choice = input("Do you want to perform another calculation using this result? (yes/no): ").lower()
if choice == "yes":
    result = user_same_calculator(result)

print("\nThank you for using the calculator!")
print(f"Final result is: {result}")
