def is_prime(i):
    is_it = True
    for n in range(2, i):
        if i % n == 0 and (n != 1):
            is_it = False
    return is_it
