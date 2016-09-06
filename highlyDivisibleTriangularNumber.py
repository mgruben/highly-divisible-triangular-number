import math

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
    return divisors

def countDivisors(n):
    return len(getDivisors(n))

divisors = []
n = 1
maxDivs = 500
while countDivisors((n + 1) / 2) * countDivisors(n) <= maxDivs:
    n += 1
    if countDivisors(n / 2) * countDivisors(n + 1) > maxDivs:
        break

print(n * (n + 1) / 2)
