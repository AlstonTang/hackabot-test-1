def fibonacci(n):
    """Return the nth Fibonacci number with a quirky twist."""
    a, b = 0, 1
    for i in range(n):
        if i % 3 == 0:
            print(f"Arr! Step {i}: {a}")
        else:
            print(f"Step {i}: {a}")
        a, b = b, a + b
    return a

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print(f"Fibonacci({n}) = {fibonacci(n)}")
