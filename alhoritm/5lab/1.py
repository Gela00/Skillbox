# Вводим строку aabaabaabaabaa
I = "Abcab"

# Создаем словарь для хранения подстрок
substrings = {}

# Проходим по всем возможным длинам подстрок
for L in range(1, len(I) + 1):
    # Создаем словарь для подсчета подстрок текущей длины
    count = {}

    # Проходим по всем подстрокам текущей длины
    for i in range(len(I) - L + 1):
        # Получаем подстроку
        substring = I[i:i + L]

        # Если подстрока уже есть в словаре, увеличиваем ее количество
        if substring in count:
            count[substring] += 1
        # Иначе добавляем подстроку в словарь
        else:
            count[substring] = 1

    # Добавляем максимальное количество повторений подстрок текущей длины в словарь подстрок
    substrings[L] = max(count.values())

# Находим максимальный вес подстрок
max_weight = max(L * count for L, count in substrings.items())

print(max_weight)
