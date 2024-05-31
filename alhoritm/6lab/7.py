'''def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def min_numbers_after_operations(L, N, numbers):
    # Создаем множество для хранения уникальных чисел после операций
    unique_numbers = set(numbers)

    # Проходим по каждому числу
    for num in bubble_sort(list(unique_numbers)): '''

def min_numbers_after_operations(L, N, numbers):
    unique_numbers = set()

    for num in (numbers):
        # Если число уже есть в множестве, пропускаем его
        if num in unique_numbers:
            continue

        if num + L in unique_numbers:
            unique_numbers.remove(num + L)
        elif num - L in unique_numbers:
            unique_numbers.remove(num - L)
        else:
            unique_numbers.add(num)

    return len(unique_numbers)

L = 10
N = 3
numbers = [11, 21, 27]
print(min_numbers_after_operations(L, N, numbers))  # 1

L = 5
N = 3
numbers = [6, 10, 27]
print(min_numbers_after_operations(L, N, numbers))  # 2

L = 5
N = 3
numbers = [5, 0, 10]
print(min_numbers_after_operations(L, N, numbers))  # 1

