#task3 алгоритм Евклида поиска наибольшего общего делителя
def euclid(a, b):
    if a == 0 or b == 0:
        return a + b
    if a > b:
        return euclid(a - b, b)
    else:
        return euclid(a, b - a)

print(euclid(14, 21))