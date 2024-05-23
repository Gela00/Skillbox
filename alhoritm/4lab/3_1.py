# Списки для хранения имен пользователей и их номеров телефонов
users = []
phone_numbers = []

# Количество команд
# N = int(input())
N = 4

# Команды
for _ in range(N):
    command = input().split()

    if command[0] == "ADD":
        if command[1] in users:
            print("ERROR")
        # Иначе добавляем пользователя и его номер телефона
        else:
            users.append(command[1])
            phone_numbers.append(command[2])

    elif command[0] == "DELETE":
        # Если пользователь существует, удаляем его и его номер телефона
        if command[1] in users:
            index = users.index(command[1])
            users.pop(index)
            phone_numbers.pop(index)
        else:
            print("ERROR")

    elif command[0] == "EDITPHONE":
        if command[1] in users:
            index = users.index(command[1])
            phone_numbers[index] = command[2]
        else:
            print("ERROR")

    elif command[0] == "PRINT":
        if command[1] in users:
            index = users.index(command[1])
            print(users[index], phone_numbers[index])
        else:
            print("ERROR")
