# аттракционы кресла
def solve():
    # Читаем размеры аттракциона
    N, M = map(int, input().split())
    # Читаем состояние аттракциона после сеанса
    grid = [list(map(int, input().split())) for _ in range(N)]
    # Создаем списки для хранения текущего положения рядов и колонок
    rows = [i for i in range(N)]
    cols = [i for i in range(M)]
    # Создаем список для хранения операций
    operations = []
    # Проходим через каждую ячейку
    for i in range(N):
        for j in range(M):
            # Вычисляем ожидаемый номер кресла
            expected = i * M + j + 1
            # Если кресло не на своем месте
            if grid[rows[i]][cols[j]] != expected:
                # Ищем правильное место для кресла
                for x in range(i, N):
                    for y in range(j, M):
                        if grid[rows[x]][cols[y]] == expected:
                            # Если кресло в другом ряду, меняем ряды
                            if x != i:
                                rows[i], rows[x] = rows[x], rows[i]
                                operations.append(('R', i + 1, x + 1)) #индексы начинаются с нуля, поэтому при выводе операций к индексам добавляется 1. Это сделано для соответствия формату входных и выходных данных
                            # Если кресло в другой колонке, меняем колонки
                            if y != j:
                                cols[j], cols[y] = cols[y], cols[j]
                                operations.append(('C', j + 1, y + 1))
                            break
    # Выводим количество операций
    print(len(operations))
    # Выводим операции
    for op in operations:
        print(*op)

# Запускаем функцию solve
solve()