#охранники
def guard(K, N):
    for _ in range(K):
        guards = [0] * 10001
        # Создаем список для хранения времени прихода и ухода каждого охранника
        times = []
        for _ in range(N):
            # время прихода и ухода охранника
            A, B = map(int, input().split())
            times.append((A, B))
            # Если охранник присутствует прибавляем
            for i in range(A, B):
                guards[i] += 1
        # Есть ли хотя бы один охранник в каждый промежуток времени
        if all(guards[i] > 0 for i in range(10000)):

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

k = 1
N = 2
guard(1, 2)

