#task8 Убрать специальные символы из ввода номера
s = '+7 (812) 123-42-42'
s2 = ''.join(filter(str.isalnum, s))
print('+',s2)

