# Хранение телефонной книги

phone_book = {}

# Количество команд
# N = int(input())
N = 4

# Команды
for _ in range(N):
    command = input().split()

    if command[0] == "ADD":
        if command[1] in phone_book:
            print("ERROR")
        else:
            phone_book[command[1]] = command[2]

    elif command[0] == "DELETE":
        if command[1] in phone_book:
            del phone_book[command[1]]
        else:
            print("ERROR")

    elif command[0] == "EDITPHONE":
        if command[1] in phone_book:
            phone_book[command[1]] = command[2]
        else:
            print("ERROR")

    elif command[0] == "PRINT":
        if command[1] in phone_book:
            print(command[1], phone_book[command[1]])
        else:
            print("ERROR")
