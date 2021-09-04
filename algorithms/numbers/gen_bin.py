def gen_bin(m, prefix=""):
    if m == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(m - 1, prefix + digit)

