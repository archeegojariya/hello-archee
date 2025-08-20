history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    print("Simple Calculator")
    while True:  # <-- Added this line to start the loop
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /, ^): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operator"

        print("Result:", result)

      history.append(f"{num1} {op} {num2} = {result}")

        cont = input("Do you want to perform another calculation? (y/n): ")  # <-- Added this line
        if cont.lower() != 'y':  # <-- Added this line to break the loop
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
