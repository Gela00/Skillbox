def match(pattern, string):
    # Если оба пустые, то совпадение найдено
    if not pattern and not string:
        return True
    # Если оба не пустые и первые символы совпадают
    elif pattern and string and (pattern[0] == string[0] or pattern[0] == '?'):
        return match(pattern[1:], string[1:])
    # Если в шаблоне есть *, то проверяем два случая:
    # 1) * сопоставляется с текущим символом строки
    # 2) * сопоставляется с пустой строкой
    elif pattern and pattern[0] == '*':
        return match(pattern[1:], string) or (string and match(pattern, string[1:]))
    # Во всех остальных случаях совпадение не найдено
    else:
        return False

# имя файла и образец
filename = input()
pattern = input()

# Сопоставляем имя файла с образцом
if match(pattern, filename):
    print("YES")
else:
    print("NO")
