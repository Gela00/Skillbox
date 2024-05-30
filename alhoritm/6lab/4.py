
# проверки простых чисел
def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

# Функция для нахождения наименьшего числа K
def find_K(M, N):
    # Создаем массив для хранения простых чисел
    primes = []
    # Начальное значение K
    K = 2
    # Пока длина массива не равна M
    while len(primes) != M:
        # Очищаем массив
        primes = []
        # Проверяем каждое число в диапазоне от K до K+N
        for num in range(K, K+N):
            # Если число простое, добавляем его в массив
            if is_prime(num):
                primes.append(num)
        # Увеличиваем K на 1
        K += 1
    # Если такого числа не существует или оно больше 2*10^7, возвращаем -1
    return -1 if K > 2*10**7 else K-1

# Тестирование функции
print(find_K(4, 10))  # 3
print(find_K(3, 15))  # 14

