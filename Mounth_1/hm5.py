for i in range(1, 6):
    print(0)

for i in range(1, 101):
    print(i)

for i in range(1, 497):
    if i % 2 == 0:
        print(f'Число {i} чётное')
    else:
        print(f'Число {i} нечётное')

name = list(range(1, 1001))
minimum = (min(name))
maximum = (max(name))
draw = (sum(name))
print(f' {draw} - общая сумма,\n {minimum} - минимальная сумма,\n {maximum} - максимальная сумма')

spisok = []
for i in range(100):
    spisok.append(0)
print(spisok)

per_1 = 12
per_2 = 20
print(f'текущая значения: per_1 = {per_1} и per_2 = {per_2}')
per_3 = int(input(f"Поменяйте местами значения: per_1 = "))
per_4 = int(input(f"Поменяйте местами значения: per_2 = "))
print(f"обновленная версия: per_1 = {per_3}, per_2 = {per_4}")

letters = 'ЫмВЫоЯСлоДШдНККеАЩЙцФ'
for text in letters:
    if not text.isupper():
        print(text, end='')
