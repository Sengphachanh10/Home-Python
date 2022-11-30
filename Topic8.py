def endgame(start, end):
    out = list()
    if start <= 1:
        start = 2

    sieve = [True] * (end + 1)
    for p in range(start, end + 1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, end + 1, p):
                sieve[i] = False
    return out

print(endgame(2, 1000))