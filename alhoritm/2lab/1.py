#максимальное произведение любых трех чисел
'''def solve():
    # Читаем количество чисел
    N = int(input())
    # Читаем числа
    numbers = [int(input()) for _ in range(N)]
    # Сортируем числа
    numbers.sort()
    # Максимальное произведение может быть достигнуто либо путем умножения трех наибольших чисел,
    # либо путем умножения двух наименьших (отрицательных) чисел на наибольшее число.
    # Вычисляем оба варианта и выбираем максимальное.
    max_product = max(numbers[-1] * numbers[-2] * numbers[-3], numbers[0] * numbers[1] * numbers[-1])
    # Выводим максимальное произведение
    print(max_product)

# Запускаем функцию solve
solve()'''

#сортировка пузырьком по убыванию
def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def multiply_largest_three(arr):
    bubble_sort_desc(arr)
    result = 1
    #ищем перемножаем 3 самых больших
    for i in range(3):
        result *= arr[i]
    return result

# Пример использования
my_array = [-1, 2, 3, -4, -2, 5, -1, 5, -3, -2]
result = multiply_largest_three(my_array)
print("Результат умножения трех самых больших чисел в массиве:", result)