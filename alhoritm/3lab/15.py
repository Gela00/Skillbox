#провода
#разрезать на кусочки и получить максимальную найти макс длину
def max_length(N, K, wires):
    # задаем мин и макс длину кусочка
    min_wire, max_wire = 1, max(wires)

    while min_wire <= max_wire:
        #сред длина
        mid = (min_wire + max_wire) // 2
        # сколько можно получить кусочков если разделить на кусочки длинной mid
        pieces = sum(wire // mid for wire in wires)
        if pieces >= K:
            # Если колво кусочков достаточно, увеличить длину
            min_wire = mid + 1
        else:
            # Если колво кусочков недостаточно, уменьшим длину
            max_wire = mid - 1

    # макс длина
    return max_wire

# N - колво проводов
N, K = 5, 7
wires = [15, 12, 5, 13, 6]
print(max_length(N, K, wires))
