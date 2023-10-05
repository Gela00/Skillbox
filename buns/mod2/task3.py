a = float(input())
b = float(input())
c = float(input())
if a > b > c or c > b > a:
    s = b
elif a > c > b or b > c > a:
    s = c
else:
    s = a
print(s)