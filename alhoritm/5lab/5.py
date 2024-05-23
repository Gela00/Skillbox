def bubble_sort(items):
    # Проходим по всем элементам списка
    for i in range(len(items)):
        for j in range(len(items) - 1):
            # Если текущий элемент больше следующего
            if items[j][1] < items[j + 1][1] or (items[j][1] == items[j + 1][1] and items[j][0] > items[j + 1][0]):
                # Меняем их местами
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

# Вводим количество клиентов и значение параметра R
# K, R = map(int, input().split())
K, R = 3, 5

# Создаем список для хранения координат клиентов
clients = [list(map(int, input().split())) for _ in range(K)]

# Создаем словарь для подсчета количества клиентов, которые могут быть обслужены каждой станцией
stations = {}

# Проходим по всем клиентам
for i in range(K):
    # Проходим по всем остальным клиентам
    for j in range(i+1, K):
        # Вычисляем расстояние между клиентами
        distance = ((clients[i][0] - clients[j][0]) ** 2 + (clients[i][1] - clients[j][1]) ** 2) ** 0.5
        # Если расстояние не больше R
        if distance <= R:
            # Увеличиваем количество клиентов, которые могут быть обслужены каждой станцией
            stations[i] = stations.get(i, 0) + 1
            stations[j] = stations.get(j, 0) + 1

# Сортируем станции по количеству обслуживаемых клиентов в порядке убывания
stations = bubble_sort(list(stations.items()))

# Выводим номера станций и количество обслуживаемых клиентов
for station, clients in stations[:10]:
    print(station, clients)
