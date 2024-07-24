print("+ - Add")
print("- - Subtract")
print("* - Multiply")
print("/ - Divide")

option = input("Choose an operation: ")

if option in ['+', '-', '*', '/']:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if option == '+':
        result = num1 + num2
    elif option == '-':
        result = num1 - num2
    elif option == '*':
        result = num1 * num2
    elif option == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            result = None
    print("The result of the operation is {}".format(result))
else:
    print("Invalid operation entered")