'''
# Вводим количество элементов в массиве и количество запросов
N, M = map(int, input().split())

# Создаем массив с элементами
V = np.array(list(map(int, input().split())))
'''
N, M = 10, 2
V = [1, 7, 15, 8, 9, 15, 15, 19, 5, 19]
results = []

for _ in range(M):
    request = list(map(int, input().split()))
    # request = [1, 1, 3]
    l = request[1]
    r = request[2]
    if request[0] == 1:
        # сумма элементов от V[L] до V[R] включительно
        #print(np.sum(V[l-1:r]))
        results.append(sum(V[l - 1:r]))

    elif request[0] == 2:
        # Меняем значение элемента массива
        V[request[1] - 1] = request[2]
        print(V)

for result in results:
    print(result)