# N эталонных множеств,
# M размер каждого из множеств и
# K количество пробных множеств
#N, M, K = map(int, input().split())
N, M, K = 1, 2, 3

# Эталонные множества
reference_sets = []

for _ in range(N):
    reference_set = set(map(int, input().split()))
    reference_sets.append(reference_set)

results = []

# Пробные множества
for _ in range(K):
    test_set = set(map(int, input().split()))

    # Проверяем, совпадает ли пробное множество с каким-либо из эталонных множеств
    if test_set in reference_sets:
        results.append(1)
    else:
        results.append(0)

for result in results:
    print(result)
