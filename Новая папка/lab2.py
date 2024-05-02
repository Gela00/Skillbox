'''Даны два упорядоченных по неубыванию массива.
Требуется найти количество таких элементов, которые присутствуют в обоих массивах.
Первая строка содержит размеры массивов N1 и N2.
В следующих N1 строках содержатся элементы первого массива,
в следующих за ними N2 строках – элементы второго массива.
Программа должна вывести ровно одно число – количество общих элементов.'''

def count(list):
    dict = {}  #пустой словарь
    for i in list:
        v = dict.get(i, 0) #считает появление каждого элемента, иначе 0
        dict[i] = v + 1
    return dict

n1, n2 = map(int, input().split())
list1 = []
list2 = []

for i in range(n1):
    num = int(input())
    list1.append(num)

for i in range(n2):
    num = int(input())
    list2.append(num)

#сохраняем все повторяющиеся элементы
same_el = []
d = count(list2)
for i, v in count(list1).items():
    w = d.get(i, 0)
    for j in range(min(v, w)):
        same_el.append(i)

print(len(same_el))