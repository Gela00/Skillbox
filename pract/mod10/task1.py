import re


# пароль должен содержать только латинские символы, цифры и специальные символы ^$%@#&*!?
# пароль должен состоять из не менее чем шести символов
# пароль должен содержать по крайней мере два латинских символа в верхнем регистре
# пароль должен содержать по крайней мере одну цифру
# пароль должен содержать по крайней мере два различных специальных символа
# пароль не должен содержать трех одинаковых символов подряд

def func(string: str) -> bool:
    if re.search(r'[a-zA-Z0-9^$%@#&*!?]', string):  # лат, цифры и спец символы
        return True

    if re.match(r'[A-Z]{2,}', string):  # два сивола в верхнем регистре
        return True

    if len(string) >= 6:  # длина
        return True

    if re.search(r'\d', string):  # хотя бы цифра
        return True

    if len(set(re.findall(r'[^^$%@#&*!?]', string))) >= 2:
        return True

    if not re.search(r'(.)\1\1', string):  # не более двух одинаковых вместе
        return True

    else:
        return False

print(func('enroi#$rkdeR#$092uWedchf34tguv394h'))

