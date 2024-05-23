import math

# N = int(input())
N = 10
# Обрабатываем числа
for i in range(N):
    # Вводим число
    number = int(input())

    # Вычисляем квадратный корень числа
    root = math.sqrt(number)

    # Если квадратный корень является целым числом, то число является полным квадратом
    if root == int(root):
        print(i + 1)
