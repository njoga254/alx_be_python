def perform_operation(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Division":
        if num2 == 0:
            return "Error: Division by zero is impossible"
        else:
            return num1 / num2
    elif operation == "Multiplication":
        return num1 * num2

