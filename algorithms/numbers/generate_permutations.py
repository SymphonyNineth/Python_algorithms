def generate_permutations(n:int, m:int = -1, prefix = None):
    def contains(number, l):
        for n in l:
            if number == n:
                return True
        return False
    m = n if m == -1 else m
    prefix = prefix or []
    if m == 0:
        print(*prefix)
        return
    for number in range(1, n + 1):

        if contains(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(n, m - 1, prefix)
        prefix.pop()
    

generate_permutations(10)