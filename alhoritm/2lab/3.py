from math import sqrt

# Функция для вычисления векторного произведения
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# Функция для сортировки массива точек
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Функция для вычисления периметра минимального охватывающего многоугольника
def perimeter(points):
    # Сортируем точки
    points = bubble_sort(points)
    lower = []
    # Строим нижнюю оболочку
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    # Строим верхнюю оболочку
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Объединяем оболочки
    hull = lower[:-1] + upper[:-1]

    # Вычисляем периметр
    perimeter = 0
    for i in range(1, len(hull)):
        perimeter += sqrt((hull[i][0] - hull[i-1][0])**2 + (hull[i][1] - hull[i-1][1])**2)
    perimeter += sqrt((hull[0][0] - hull[-1][0])**2 + (hull[0][1] - hull[-1][1])**2)

    # Возвращаем периметр, округленный до двух знаков после запятой
    return round(perimeter, 2)

points = [(2, 1), (2, 2), (2, 3), (3, 2), (1, 2)]

print(perimeter(points))  # Вывод: 5.66