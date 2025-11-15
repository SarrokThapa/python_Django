def factorial(n):
    if n == 1:  # Base case: Stop here!
        return 1
    else:       # Recursive case: Call itself with n-1
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120 (It calls: factorial(5) → 5*factorial(4) → ... → 1)