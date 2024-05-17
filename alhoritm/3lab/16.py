def intersection(set1, set2):
    result = []
    for element in set1:
        # Добавляем в списко, если элемент содержится во втором множестве
        if element in set2:
            result.append(element)

    return result

def max_intersection_size(N, sets):
    max_size = 0

    # Перебор всех пар множеств
    for i in range(N):
        for j in range(i+1, N):
            # Нахождение пересечения двух множеств
            intersection_elements = intersection(sets[i], sets[j])
            max_size = max(max_size, len(intersection_elements))

    return max_size

N1 = 4
sets1 = [[-2, 6, 8, 4, -1], [5, 3, 10, -5, -1], [7, 8, -5, -1, -2], [-1, 8, 4, 9, 0]]

N2 = 3
sets2 = [[9, 7, 1, 8], [5, 7, 6, 3], [5, 9, 8, 6]]
print(max_intersection_size(N1, sets1))
print(max_intersection_size(N2, sets2))

#ДОБАВИТЬ СОРТИРОВКУ
