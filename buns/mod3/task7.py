#task7 присутствуют ли в последовательности одинаковые числа
s = str(input())
def same(nums): return len(set(nums)) < len(nums)
print(same(s))