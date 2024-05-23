# Создаем словарь для хранения базы данных
db = {}

# Вводим количество команд
N = int(input())

# Обрабатываем команды
for _ in range(N):
    # Вводим команду и ее аргументы
    command = input().split()

    # Если команда - это ADD
    if command[0] == "ADD":
        # Если ключ уже есть в базе данных, выводим ERROR
        if command[1] in db:
            print("ERROR")
        # Иначе добавляем запись в базу данных
        else:
            db[command[1]] = command[2]

    # Если команда - это DELETE
    elif command[0] == "DELETE":
        # Если ключ есть в базе данных, удаляем его
        if command[1] in db:
            del db[command[1]]
        # Иначе выводим ERROR
        else:
            print("ERROR")

    # Если команда - это UPDATE
    elif command[0] == "UPDATE":
        # Если ключ есть в базе данных, обновляем его значение
        if command[1] in db:
            db[command[1]] = command[2]
        # Иначе выводим ERROR
        else:
            print("ERROR")

    # Если команда - это PRINT
    elif command[0] == "PRINT":
        # Если ключ есть в базе данных, выводим его и его значение
        if command[1] in db:
            print(command[1], db[command[1]])
        # Иначе выводим ERROR
        else:
            print("ERROR")
