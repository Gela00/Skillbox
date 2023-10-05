a = int(input())

b = format(a, 'b') #двоичный
o = format(a, 'o') #восьмеричный
h = format(a, 'x') #шестнадцатеричный

if a < 0:
    print('Неверный ввод')
else:
    print(b, o, h)

