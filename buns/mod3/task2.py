#task2 вывести число в разных системах счисления
a = int(input())
if a < 0: print('Неверный ввод')
else: print(bin(a), oct(a), hex(a))