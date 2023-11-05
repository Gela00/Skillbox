#task3 Создать генератор для чисел Армстронга.
def armstrong_generator():
    n = 150
    while True:
        if n == get_sum_digits(n):
            yield n
        n += 1

def get_sum_digits(num):
    sum_digits = 0   #сумма значений
    num_str = str(num)  #число в строку
    for digit in num_str:  #перебор каждого числа в строке
        sum_digits += int(digit) ** len(num_str)
    return sum_digits

generator = armstrong_generator()
def get_armstong_numbers():
    return next(generator)

for i in range(8):
    print(get_armstong_numbers(), end =" ")