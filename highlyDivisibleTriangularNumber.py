def genTriangular():
    n = 1
    m = 2
    while True:
        yield n
        n += m
        m += 1
