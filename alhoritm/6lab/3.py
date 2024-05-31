def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# точка перемещается в пределах L
# найти минимальное количество точек на одной прямой

def min_points(L, N, V):
    V = bubble_sort(V)
    print(V)
    i = 0  # текущая точка
    j = 0  # самая дальная точка, которую можно достичь из текущей точки
    min_points = N

    # пока оба указателя i и j в пределах списка V.
    while i < N and j < N:
        while j < N and V[j] - V[i] <= L:
            # Пока следующая точка в пределах диапазона L
            j += 1
        min_points = min(min_points, N - (j - i))

        i += 1
    return min_points

L = 10
N = 5
V = [30, 3, 14, 19, 21]

print("Минимальное количество точек:", min_points(L, N, V))
