def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1 or x == 2:
        return x-1
    else:
        return(fibonacci(x-1)+fibonacci(x-2))

fibonacci_series = lambda x: [fibonacci(i) for i in range(1,x+1)]
print(fibonacci_series(10)) #test