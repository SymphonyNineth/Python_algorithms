def gcd(a:int, b:int):
    assert type(a) == int and type(b) == int, "Numbers must be integers"
    assert a > 0 and b > 0, "Numbers must be greater than 0"
    if a == b:
        return a
    if(a < b):
       return gcd(b - a, a)
    if(b < a):
        return gcd(a - b, b)
    