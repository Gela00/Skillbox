s1 = '4604075024433'
s = [int(i) for i in s1] #преобразовали в числа
a1 = 0 #нечётные
a2 = 0 #чётные

for i in range(len(s)):
    if i % 2 != 0:
        a2 += s[i]
    else:
        a1 += s[i]

sum = a1 + a2 * 3
print(a1, a2 * 3, sum)

if sum % 10 == 0:
    print('yes')
else:
    print('no')


