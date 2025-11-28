def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling.
    
    Args:
        numerator: The number to be divided (can be string or number)
        denominator: The number to divide by (can be string or number)
    
    Returns:
        str: Result message or error message
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."