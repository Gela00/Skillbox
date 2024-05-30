from collections import defaultdict
import heapq
"""
    Функция для определения максимальной прибыли и списка пассажиров.
    :param N: Количество остановок.
    :param M: Количество мест в маршрутке.
    :param K: Количество пассажиров.
    :param P: Стоимость билета.
    :param passengers: Список пассажиров.
    :return: Максимальная прибыль и список пассажиров.
    """

import heapq


def max_profit(N, M, K, P, passengers):
    # Сортируем пассажиров по номеру остановки выхода
    passengers.sort(key=lambda x: x[1])

    # Инициализируем очередь и максимальную прибыль
    queue = []
    profit = 0
    in_bus = 0

    for i in range(K):
        # Добавляем пассажира в очередь
        heapq.heappush(queue, -passengers[i][0])

        # Если количество пассажиров в очереди превышает количество мест в маршрутке,
        # то удаляем пассажира с наименьшим номером остановки выхода и добавляем его стоимость к прибыли
        if len(queue) > M:
            removed = -heapq.heappop(queue)
            profit += P
            in_bus -= 1
        else:
            in_bus += 1

    # Добавляем стоимость оставшихся в очереди пассажиров к прибыли
    profit += P * len(queue)

    return profit, in_bus


# Тестовые данные
N = 6
M = 2
K = 6
P = 9
passengers = [(1, 4), (2, 6), (1, 5), (2, 3), (4, 6), (3, 6)]

profit, in_bus = max_profit(N, M, K, P, passengers)
print("Максимальная прибыль:", profit)
print("Количество пассажиров в маршрутке:", in_bus)

'''
import time
from memory_profiler import memory_usage

# Ваши тестовые данные
tests = [
    (6, 2, 6, 9, [(1, 4), (2, 6), (1, 5), (2, 3), (4, 6), (3, 6)]),
    # Добавьте здесь другие тестовые данные
]

for test in tests:
    start_time = time.time()
    start_memory = memory_usage()[0]
    profit, in_bus = max_profit(*test)
    end_time = time.time()
    end_memory = memory_usage()[0]
    print(f"Результат: {profit}, {in_bus}")
    print(f"Время выполнения: {end_time - start_time} секунд")
    print(f"Использование памяти: {end_memory - start_memory} MiB")
'''