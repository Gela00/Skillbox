s = str(input())

a0 = s.count('0')
a1 = s.count('1')
a2 = s.count('2')
a3 = s.count('3')
a4 = s.count('4')
a5 = s.count('5')
a6 = s.count('6')
a7 = s.count('7')
a8 = s.count('8')
a9 = s.count('9')

t = True
f = False
if a0 > 1 or a1 > 1 or a2 > 1 or a3 > 1 or a4 > 1 or a5 > 1 or a6 > 1 or a7 > 1 or a8 > 1 or a9 > 1:
    print(t)
else:
    print(f)