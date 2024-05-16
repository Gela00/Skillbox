def max_length(N, K, wires):
    # Инициализация границ для бинарного поиска
    left, right = 1, max(wires)

    while left <= right:
        mid = (left + right) // 2
        # Подсчет количества кусочков проводов длиной mid
        pieces = sum(wire // mid for wire in wires)
        if pieces >= K:
            # Если количество кусочков достаточно, попробуем увеличить длину
            left = mid + 1
        else:
            # Если количество кусочков недостаточно, уменьшим длину
            right = mid - 1

    # Возвращаем максимальную длину
    return right

N, K = 5, 7
wires = [15, 12, 5, 13, 6]
print(max_length(N, K, wires))
