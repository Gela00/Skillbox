#task5 Выведите ‘yes’, если количество единиц совпадает с количеством нулей
a = str(input())
a0, a1 = '0', '1'; c0, c1 = a.count(a0), a.count(a1)
print('yes' if c0 == c1 else 'no')