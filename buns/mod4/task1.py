#task1 Для списка чисел вывести одно из трех сообщений
s = str(input())
s_list = list(s.replace(" ", "")) #преобразование строки в список

if len(set(s_list)) == 1: #совпадает ли число разных чисел с длиной списка
    print("Все числа равны")
elif len(set(s_list)) > 1 and (len(set(s_list)) != len(s_list)):
    print("Есть равные и неравные числа")
else:
    print("Все числа разные")