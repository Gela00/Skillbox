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


class CustomQueue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)
        self.queue.sort()

    def pop(self):
        if len(self.queue) > 0:
            self.queue.pop(0)

    def get_min(self):
        if len(self.queue) > 0:
            return self.queue[0]
        return None

def process_commands(commands):
    queue = CustomQueue()
    results = []

    for command in commands:
        if command[0] == "+":
            queue.push(int(command[1]))
        elif command[0] == "-":
            queue.pop()
        elif command[0] == "?":
            min_element = queue.get_min()
            if min_element is not None:
                results.append(min_element)

    return results

# Тестовые данные
commands = [("+", "5"), ("+", "3"), ("?", ""), ("-", ""), ("?", ""), ("+", "2"), ("?", "")]
print(process_commands(commands))  # Вывод: [3, 5, 2]
