def factorize_number(x):
    factorized_numbers = []
    devisor = 2
    while x > 1:
        if x % devisor == 0:
            factorized_numbers.append(devisor)
            x //= devisor
        else:
            devisor += 1
    return factorized_numbers