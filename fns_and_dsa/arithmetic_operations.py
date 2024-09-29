def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "division":
        if num2 == 0:
            return "Error: Division by zero is impossible"
        else:
            return num1 / num2
    elif operation == "multiply":
        return num1 * num2

