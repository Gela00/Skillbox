# аттракцион кресла
def attraction(n, m):
    # Списки для хранения текущего положения рядов и колонок
    rows = [i for i in range(N)]
    cols = [i for i in range(M)]
    # Список для хранения операций
    operations = []

    # R - перестановкка рядов
    # С - перестановка колоннок

    # Проходим через каждую ячейку
    for i in range(N):
        for j in range(M):
            # Вычисление ожидаемого номера кресла
            expected = i * M + j + 1
            # Если кресло не на своем месте
            if grid[rows[i]][cols[j]] != expected:
                # правильное место для кресла
                for x in range(i, N):
                    for y in range(j, M):
                        if grid[rows[x]][cols[y]] == expected:
                            # Если кресло в другом ряду, меняем ряды
                            if x != i:
                                rows[i], rows[x] = rows[x], rows[i]
                                operations.append(('R', i + 1, x + 1))
                            # Если кресло в другой колонке, меняем колонки
                            if y != j:
                                cols[j], cols[y] = cols[y], cols[j]
                                operations.append(('C', j + 1, y + 1))
                            break

    # Вывод операций
    print(len(operations))

    for op in operations:
        print(*op)

# Размеры аттракциона
N, M = 2, 2

grid = [4, 3], [2, 1]
print(attraction(N, M))
