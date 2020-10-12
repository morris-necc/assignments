def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        test_list = [].append([fibonnaci(n-1),fibonnaci(n-2)])
        print(test_list)

fibonnaci(10)
#i give up