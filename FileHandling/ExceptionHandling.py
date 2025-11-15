a=10
b=0

def perform_division(x, y):
    try:
        result = x / y
    except Exception as e : #It shows all types of exceptions
        return f"Error: Division {e}"
    return result
print(perform_division(a, b))