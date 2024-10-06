

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
        return f"Result: {result:.2f}"
    
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    except ValueError:
        return "Error: Both numerator and denominator must be numeric values."

