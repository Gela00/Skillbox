def min_difference(weights):
    # сумма всех весов
    total_weight = sum(weights)
    # создание массива динамического программирования (вся сумма + 1) заполняет нулями
    dp = [0] * (total_weight + 1)

    # первый элемент делаем единицей
    dp[0] = 1

    for weight in weights:
        for i in range(total_weight, -1, -1):
            # если вес был достигнут, устанавливается 1
            if dp[i]:
                dp[i + weight] = 1

    # Ищем наименьшую разницу, начиная с половины общего веса.
    for diff in range((total_weight + 1) // 2, total_weight + 1):
        if dp[diff]:
            # возвращение минимальной разницы
            return diff - (total_weight - diff)

n = int(input())
weights = []

for i in range(n):
    num = int(input())
    weights.append(num)

print(min_difference(weights))
