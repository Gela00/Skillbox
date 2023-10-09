a = str(input())

a0 = '0'
a1 = '1'

c0 = a.count(a0) #счёт нулей
c1 = a.count(a1) #счёт единиц

if c0 == c1:
    print('yes')
else:
    print('no')
