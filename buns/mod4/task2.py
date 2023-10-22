#task2    a^n = (a^2)^n/2  при четном n,
#         a^n = a × a^n−1 при нечетном n.

def function(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return function(a, n / 2) * function(a, n / 2)
    else:
        return a * function(a, n - 1)

print(function(2, 5))
