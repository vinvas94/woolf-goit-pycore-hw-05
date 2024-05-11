def caching_fibonacci():
    # Initialize a dictionary to store computed Fibonacci numbers
    cache={}

    # Recursive function to compute Fibonacci numbers with caching
    def fibonacci(n):
        if n<=0:
            return 0
        elif n==1:
            return 1
        elif n in cache:
            return cache[n]
        else: 
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci



# Obtain the Fibonacci function with caching
fib = caching_fibonacci()

# Calculate and print Fibonacci numbers using the cached function
print(fib(10))  
print(fib(15))  
