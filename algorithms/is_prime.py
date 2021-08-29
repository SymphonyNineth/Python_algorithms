def is_prime(x):
    if x < 2:
        return False
    devisor = 2
    while devisor <= x**0.5:
        if x% devisor == 0:
            return False
        devisor += 1
    return True