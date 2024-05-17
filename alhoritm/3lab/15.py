'''
import heapq

def min_cost(N, capitals):
    # Инициализация очереди с приоритетами
    queue = []
    for capital in capitals:
        heapq.heappush(queue, capital)

    cost = 0
    # Пока в очереди больше одного элемента
    while len(queue) > 1:
        # Извлекаем два наименьших элемента
        a = heapq.heappop(queue)
        b = heapq.heappop(queue)
        # Считаем стоимость их слияния
        merge_cost = a + b + (a + b) * 0.01
        # Добавляем стоимость слияния к общей стоимости
        cost += merge_cost
        # Добавляем результат слияния обратно в очередь
        heapq.heappush(queue, merge_cost)

    # Возвращаем общую стоимость, округленную до двух знаков после запятой
    return round(cost, 2)

# Тестовые данные
N = 5
capitals = [1, 2, 3, 4, 5]
print(min_cost(N, capitals))  # Вывод: 0.33




def min_cost(N, capitals):
    # Функция для получения минимального элемента и его индекса
    def min_element(lst):
        min_val = min(lst)
        min_idx = lst.index(min_val)
        return min_val, min_idx

    # Инициализация переменной для хранения общей стоимости
    cost = 0

    # Пока в списке больше одного элемента
    while len(capitals) > 1:
        # Находим два наименьших элемента и их индексы
        min1, idx1 = min_element(capitals)
        capitals.pop(idx1)
        min2, idx2 = min_element(capitals)
        capitals.pop(idx2)

        # Считаем стоимость их слияния
        merge_cost = min1 + min2 + (min1 + min2) * 0.01
        # Добавляем стоимость слияния к общей стоимости
        cost += merge_cost
        # Добавляем результат слияния обратно в список
        capitals.append(merge_cost)

    # Возвращаем общую стоимость, округленную до двух знаков после запятой
    return round(cost, 2)

# Тестовые данные
N = 5
capitals = [1, 2, 3, 4, 5]
print(min_cost(N, capitals))  # Вывод: 0.33'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# соединить департаменты в один
def min_cost(N, capitals):
    capitals = bubble_sort(capitals)
    cost = 0

    # Пока в списке больше одного элемента
    while len(capitals) > 1:
        # Сливаем два подразделения с наименьшим капиталом
        merge = capitals[0] + capitals[1] + (capitals[0] + capitals[1]) * 0.01
        # Добавляем стоимость слияния к общей стоимости
        cost += merge * 0.01
        # Удаляем слитые и добав результат слияния в список
        capitals = capitals[2:]
        capitals.append(merge)
        capitals = bubble_sort(capitals)

    return round(cost, 2)

N = 5
capitals = [1, 2, 3, 4, 5]
print(min_cost(N, capitals))

