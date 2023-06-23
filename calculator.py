def question():
    print()
    print("Please select operation -")
    print("1. Addition \n2. Substraction \n3. Multiplication \n4. Division")

    operation_input = int(input("Select operation 1-4: "))

    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    
    if operation_input == 1:
        print(f"{num1} + {num2} =", add(num1, num2))
    elif operation_input == 2:
        print(f"{num1} - {num2} =", substract(num1, num2))
    elif operation_input == 3:
        print(f"{num1} * {num2} =", multiply(num1, num2))
    elif operation_input == 4:
        print(f"{num1} / {num2} =", divide(num1, num2))
    else:
        print("Invalid operator")

def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if __name__ == "__main__":
    question()

