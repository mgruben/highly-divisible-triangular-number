def genTriangular():
    n = 1
    m = 2
    while True:
        yield n
        n += m
        m += 1

def getDivisors(n):
    divisors = []
    if n == 1:
        divisors.append(1)
    else:
        divisors.append(1)
        divisors.append(n)
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            divisors.append(i)
    return sorted(divisors)


divisors = []
genny = genTriangular()
while len(divisors) <= 500:
    divisors = getDivisors(next(genny))
