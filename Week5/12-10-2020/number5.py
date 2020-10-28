def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1 or x == 2:
        return x-1
    else:
        return(fibonacci(x-1)+fibonacci(x-2))

fibonacci_series = lambda x: 0 if x==1 else(x-1 if x==1 or x==2 else fibonacci_series(x-1)+fibonacci_series(x-2))
print_series = lambda function, length: [function(i) for i in range(1,length+1)]
print(print_series(fibonacci_series, 10))
fibonacci_2 = lambda y: [fibonacci(i) for i in range(1,y+1)]
print(fibonacci_2(10))
