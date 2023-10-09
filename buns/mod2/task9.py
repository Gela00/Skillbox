s = str(input())
a = 0 #гласные
b = 0 #согласные
for letter in s:
    if letter == "а" or letter == "у" or letter == "е" or letter == "ы" or letter == "о" or letter == "э" or letter == "я" or letter == "и" or letter == "ю" or letter == "ё":
        a += 1
    else:
        b += 1

print(a, b)
