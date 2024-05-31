def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    #если делитель больше чем корень значит простое
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True

# нахождения числа от которого идет наименьшее колво простых в диапазоне
def find_K(M, N):
    primes = []
    K = 2
    while len(primes) != M:
        primes = []
        for num in range(K, K+N):
            if is_prime(num):
                primes.append(num)
        K += 1
    return -1 if K > 2*10**7 else K-1

print(find_K(4, 10))  # 3
print(find_K(3, 15))  # 14

