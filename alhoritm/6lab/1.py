"""Алгоритм Кадане — это метод динамического программирования, используемый для нахождения максимальной суммы подмассива в одномерном массиве.
"""
def max_subarray_sum(V):
    """
    Функция для нахождения максимальной суммы подмассива с использованием алгоритма Кадана.
    :param V: Список целых чисел.
    :return: Максимальная сумма подмассива.
    """
    # текущая сумма и максимальная суммы
    current_sum = max_sum = V[0]

    # начиная со второго элемента
    for num in V[1:]:
        # Если текущая сумма становится отрицательной, сбрасываем ее до текущего числа
        current_sum = max(num, current_sum + num)
        # Если текущая сумма больше максимальной суммы, обновляем максимальную сумму
        max_sum = max(max_sum, current_sum)

    return max_sum

p = [-4, 4, 3, 3, -4, 1, 2, 1, -4, 0]
print(max_subarray_sum(p))

import time
import random
from memory_profiler import memory_usage


def test_max_subarray_sum():
    """
    Функция для тестирования max_subarray_sum с различными тестовыми случаями.
    """
    #test_cases = [random.sample(range(-2 * 10 ** 9, 2 * 10 ** 9), 100) for _ in range(10)]
    test_cases = [
        [-4, 4, 3, 3, -4, 1, 2, 1, -4, 0],
        [-1, -2, -3, -4, -5],
        [2000000, 30000, -2, -3, 4, -100000, 2, 3, 6, -5, -2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 2, 3, 4, 5, 6000, 7, 80000, 9, 10],
        [-1, 2, -3, 40, -50, 6, -7, 8, -9, 10],
        [9**9, -2, 3, -200, 0, 5, -15],
        [2, 3, 4, 5, 7, -8, 7**9, -20, 25],
        [15, -30, 15, -10, 20, -30],
        [1, -1, 1, -1, 1, -1, 1, -1, 1]
    ]

    for i, test_case in enumerate(test_cases, 1):
        start_time = time.time()
        start_mem = memory_usage()[0]
        result = max_subarray_sum(test_case)
        end_time = time.time()
        end_mem = memory_usage()[0]
        print(
            f"Test case {i}: Время выполнения: {end_time - start_time} секунд, Использование памяти: {end_mem - start_mem} MiB, Результат: {result}")
test_max_subarray_sum()


'''print(f"Тест {i}:")
        print(f"Результат: {result}")
        print(f"Время выполнения: {end_time - start_time} секунд")
        print(f"Использование памяти: {end_mem - start_mem} MiB")
        print("-" * 50)'''
