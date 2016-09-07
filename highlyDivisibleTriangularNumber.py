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
divs = 0
while divs <= maxDivs:
    n += 1
    if n % 2 == 0:
        divs = countDivisors(n / 2) * countDivisors(n + 1)
    else:
        divs = countDivisors((n + 1) / 2) * countDivisors(n)

print("The first triangular number with more than " + str(maxDivs) \
    + " divisors is " + str(n * (n + 1) // 2) + " (" + str(divs) \
    + " divisors)")
