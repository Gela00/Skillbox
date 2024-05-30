# Количество полосок для каждой цифры
stripes = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def min_and_max_numbers(N, K):
    # Инициализация таблицы динамического программирования
    dp_min = [[float('inf')] * (K + 1) for _ in range(N + 1)]
    dp_max = [[float('-inf')] * (K + 1) for _ in range(N + 1)]
    dp_min[0][0] = dp_max[0][0] = 0

    #loat('inf') используется в качестве начального значения для минимального числа в таблице динамического программирования. Это делается для того, чтобы любое другое число, которое мы сравниваем с ним, было меньше.
    # Таким образом, float('inf') здесь используется как заполнитель для “максимально возможного числа”.

    # Заполнение таблицы динамического программирования
    for i in range(1, N + 1):
        for k in range(K + 1):
            for digit, s in enumerate(stripes):
                if k >= s:
                    dp_min[i][k] = min(dp_min[i][k], dp_min[i - 1][k - s] * 10 + digit)
                    dp_max[i][k] = max(dp_max[i][k], dp_max[i - 1][k - s] * 10 + digit if dp_max[i - 1][k - s] != float('-inf') else -1)

    # Возвращаем минимальное и максимальное числа
    return dp_min[N][K] if dp_min[N][K] != float('inf') else -1, dp_max[N][K] if dp_max[N][K] != float('-inf') else -1

# Пример
N = 5
K = 15
min_number, max_number = min_and_max_numbers(N, K)
print(min_number)  # Вывод: 10117
print(max_number)  # Вывод: 97111
