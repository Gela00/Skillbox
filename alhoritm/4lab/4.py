def bubble_sort(s):
    s = list(s)
    for i in range(len(s)):
        for j in range(len(s) - 1):
            # Если текущий элемент больше следующего
            if s[j] > s[j + 1]:
                # Меняем их местами
                s[j], s[j + 1] = s[j + 1], s[j]

    # Преобразуем список обратно в строку
    return ''.join(s)

# N - Количество слов
N = 8
anagrams = {}

for _ in range(N):
    word = bubble_sort(input())

    # Если отсортированное слово уже есть в словаре, увеличиваем его количество
    if word in anagrams:
        anagrams[word] += 1
    # Иначе добавляем отсортированное слово в словарь
    else:
        anagrams[word] = 1

print(len(anagrams))
