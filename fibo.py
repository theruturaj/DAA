def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib_prev = 0
    fib_curr = 1

    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev, fib_curr = fib_curr, fib_next

    return fib_curr

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
n = 10
iterative_result = fibonacci_iterative(n)
recursive_result = fibonacci_recursive(n)

print(f"The {n}-th Fibonacci number (iterative) is: {iterative_result}")
print(f"The {n}-th Fibonacci number (recursive) is: {recursive_result}")

