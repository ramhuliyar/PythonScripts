

def fibonacci(n):
    """Return a list containing the Fibonacci series upto n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b

    return result

fibonacci_list = fibonacci(100)
fibonacci_list.sort(key=lambda x: x**2, reverse=True)
print(fibonacci_list)
