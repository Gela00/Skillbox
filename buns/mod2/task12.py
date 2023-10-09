s = '+7 (812) 123-42-42'

print(s)
s2 = ''.join(filter(str.isalnum, s))
print('+',s2)


