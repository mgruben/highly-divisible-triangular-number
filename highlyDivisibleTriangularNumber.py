import math

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
    sq = math.ceil(math.sqrt(n))
    if n // sq == sq:
        divisors.append(sq)
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    return sorted(divisors)


divisors = []
genny = genTriangular()
tri = 0
while len(divisors) <= 500:
    tri = next(genny)
    divisors = getDivisors(tri)
print(tri)
