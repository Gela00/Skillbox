# rgb: комбинация из трёх целых чисел (от 0 до 255) или трёх процентных значений (от 0% до 100%), перечисленных через запятую.
# hex: шестизначное представление цвета в RGB пространстве. (rr) – представляют собой красное значение, следующие две – зелёное значение (gg), а последние – синее значение (bb). Перед значениями каналов предшествует символ #.
# hsl: Тон – целое число в диапазоне от 0 до 360, насыщенность и светлота
import re
def type_color(color: str) -> bool:

    # rgb
    if bool(re.match(r'rgb', color)):
        pattern = re.compile(r'^rgb\((\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?), (\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?), (\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?)\)$')
        # Начало с rgb, 3 числа через запятую с с ограничением до 250
        match = re.search(pattern, color)
        if match:
            return True
        else:
            return False

    # hex
    if bool(re.match(r'#', color)):
        pattern = re.compile(r'^#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$')
        # начало с #, либо 6 цифр, либо сокращено 3
        return bool(pattern.match(color))

    # hsl
    if bool(re.match(r'hsl', color)):
        pattern = re.compile(r'^hsl\((\d{1,3}|[1-9]\d{0,2}),\s*(100%|[1-9]?\d%|0%),\s*(100%|[1-9]?\d%|0%)\)$')
        # начало с hsl, 3 числа до 360, первое целое, остальные с плавающей
        return bool(pattern.match(color))
    else:
        return False

print(type_color('#21f48D'))
print(type_color('hsl(0, 0%, 0%)'))
print(type_color('rgb(257, 50, 10)'))

