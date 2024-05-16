#охранники

def solve():
    # Читаем количество тестов
    K = int(input())
    for _ in range(K):
        # Читаем количество охранников
        N = int(input())
        # Создаем массив для отслеживания присутствия охранников
        guards = [0] * 10001
        # Создаем список для хранения времени прихода и ухода каждого охранника
        times = []
        for _ in range(N):
            # Читаем время прихода и ухода охранника
            A, B = map(int, input().split())
            times.append((A, B))
            # Увеличиваем счетчик для каждого промежутка времени, когда охранник присутствует
            for i in range(A, B):
                guards[i] += 1
        # Проверяем, есть ли хотя бы один охранник в каждый промежуток времени
        if all(guards[i] > 0 for i in range(10000)):
            # Проверяем, что удаление любого охранника приводит к появлению промежутка времени, когда объект не охраняется
            for A, B in times:
                for i in range(A, B):
                    guards[i] -= 1
                if any(guards[i] == 0 for i in range(10000)):
                    print('Accepted')
                    break
                for i in range(A, B):
                    guards[i] += 1
            else:
                print('Wrong')
        else:
            print('Wrong')

# Запускаем функцию solve
solve()

