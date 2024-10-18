# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method for adding two numbers
    @staticmethod
    def add(a, b):
        return a + b

    # Class method for multiplying two numbers
    @classmethod
    def multiply(cls, a, b):
        # Access and print the class attribute
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Demonstration of using both methods
if __name__ == "__main__":
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"Product: {product_result}")
