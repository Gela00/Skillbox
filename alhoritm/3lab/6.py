'''def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def process_commands(commands):
    queue = []
    results = []

    for command in commands:
        if command[0] == "+":
            queue.append(int(command[1]))

        elif command[0] == "-":
            queue.pop(0)

        elif command[0] == "?":
            queue = bubble_sort(queue)
            results.append(queue[0])
    return results

commands = [("+", "5"), ("+", "3"), ("?", ""), ("-", ""), ("?", ""), ("+", "2"), ("?", "")]
print(process_commands(commands))'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

class Queue:
    def __init__(self):
        self.queue = []

    #добавление элемента
    def push(self, element):
        self.queue.append(element)

    # удаление элемента
    def pop(self):
        if len(self.queue) > 0:
            self.queue.pop(0)

    # мин элемент
    def get_min(self):
        self.queue = bubble_sort(self.queue)
        if len(self.queue) > 0:
            return self.queue[0]
        return None

def process_commands(commands):
    queue = Queue()
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

commands = [("+", "5"), ("+", "3"), ("?", ""), ("-", ""), ("?", ""), ("+", "2"), ("?", "")]
print(process_commands(commands))
