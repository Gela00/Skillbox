def process_commands(commands):
    # Инициализация пустой очереди и списка для хранения результатов
    queue = []
    results = []

    # Обработка команд
    for command in commands:
        if command[0] == "+":
            # Добавление элемента в очередь
            queue.append(int(command[1]))
            # Сортировка очереди в порядке возрастания
            queue.sort()
        elif command[0] == "-":
            # Удаление элемента из очереди
            queue.pop(0)
        elif command[0] == "?":
            # Добавление минимального элемента в результаты
            results.append(queue[0])
    return results

# Тестовые данные
commands = [("+", "5"), ("+", "3"), ("?", ""), ("-", ""), ("?", ""), ("+", "2"), ("?", "")]
print(process_commands(commands))  # Вывод: [3, 5, 2]
