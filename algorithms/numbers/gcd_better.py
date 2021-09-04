def gcd_better(a:int, b:int):
    assert type(a) == int and type(b) == int, "Numbers must be integers"
    return a if b == 0 else gcd_better(b, a % b)