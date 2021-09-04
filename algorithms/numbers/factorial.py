def factorial(n):
    assert n >= 0, "Factorial isn't defined for negative numbers"
    if n <= 1:
        return 1
    return n * factorial(n - 1)