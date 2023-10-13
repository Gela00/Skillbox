#task3 Вывести все домены по порядку
a = str(input())
s = (a.split("."));s3 = s[0];s[0] = s[2];s[2] = s3;print('\n'.join(s))