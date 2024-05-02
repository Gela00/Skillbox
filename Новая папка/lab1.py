'''set_A = set()
set_B = set()
input_data = input().split()
split_index = input_data.index('0')
for num in input_data[:split_index]:
    set_A.add(int(num))

for num in input_data[split_index]:
    set_B.add(int(num))

symmetric_difference = sorted((set_A - set_B) | (set_B - set_A))
symmetric_difference = symmetric_difference[1:]
print(set_A, set_B)
print(symmetric_difference)

if symmetric_difference:
    print(''.join(map(str, symmetric_difference)))
else:
    print(0)
#1 2 3 4 5 0 1 7 5 8 0'''


def symmetric_difference(input_data):
    # Преобразуем входные данные в список чисел
    numbers = list(map(int, input_data.split()))

    # Находим индекс разделителя (0)
    separator = numbers.index(0)

    # Создаем два множества: A и B
    set_A = set(numbers[:separator])
    # "+1" означает, что начинаем с элемента, следующего после значениz переменной "separator" включительно,
    # "-1" означает, что заканчиваем перед последним элементом.
    # Таким образом, данный срез охватывает все элементы списка, начиная с элемента следующего за "separator" и до предпоследнего элемента включительно.
    set_B = set(numbers[separator + 1:-1])
    print(set_A)
    print(set_B)

    # Вычисляем симметрическую разность множеств A и B
    difference = set_A.symmetric_difference(set_B)

    # Сортируем результат по возрастанию  и преобразуем его обратно в список
    sorted_difference = list(difference)
    n = 1
    while n < len(sorted_difference):
        for i in range(len(sorted_difference) - n):
            if sorted_difference[i] > sorted_difference[i + 1]:
                sorted_difference[i], sorted_difference[i + 1] = sorted_difference[i + 1], sorted_difference[i]
        n += 1

    # Если получившееся множество пусто, возвращаем [0]
    if not sorted_difference:
        return [0]

    # Возвращаем отсортированную симметрическую разность
    return sorted_difference


# Пример использования функции
input_data = "2 1 6 8 7 3 0 4 1 6 2 3 9 0"
print(symmetric_difference(input_data))
