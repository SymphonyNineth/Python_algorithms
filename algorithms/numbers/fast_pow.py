def pow(a:float, n:int):
    print(n)
    print("result " + str(a))
    if(n == 0):
        return 1
    elif(n % 2 == 1):
        return a * pow(a, n - 1)
    # n is even
    else:
        return a * pow(a ** 2, n // 2)
    
#incorrect
#Must be debugged