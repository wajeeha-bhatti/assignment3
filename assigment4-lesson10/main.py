# main.py

def divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Please provide numbers only.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print("Division successful!")
    finally:
        print("Execution completed.\n")

# Test cases
divide(10, 2)     # Normal case
divide(5, 0)      # Division by zero
divide("10", 2)   # Invalid type
