

def safe_divide(numerator, denominator):
    """
    Safely performs division between two numbers, handling ZeroDivisionError and ValueError.

    Parameters:
    numerator: The numerator for division.
    denominator: The denominator for division.

    Returns:
    str: A message indicating the result of the division or an appropriate error message.
    """
    try:
        
        num = float(numerator)
        denom = float(denominator)
        
        
        result = num / denom
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."

