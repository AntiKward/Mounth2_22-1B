hm1 = open('hm8_1.txt', 'r', encoding='utf-8') #hm1
reading = hm1.read()
print(reading)
hm1.close()

hm2 = open('hm8_1.txt', 'r', encoding ='utf-8') #hm2, #hm6
for item in hm2:
  print(len(item))
hm2.close()

name = str(input('Введите имя: '))
main_name = open('hm8_4.txt', '+a', encoding ='utf-8') #hm4
main_name.write(f'{name}\n ')
print(f'{name}')
main_name.close()

user_search = str(input('Введите имя которое хотите найти: ')) #hm3
hm4 = open('hm8_4.txt', 'r', encoding = 'utf-8')
reading_4 = hm4.read()
if user_search in reading_4:
    print(f'{user_search} находится в списке')
else:
    print('ошибка')

with open('hm8_1.txt','r') as hm5_1, open('hm8_4.txt','a') as hm5_2: #hm5
  for i in hm5_1:
    hm5_2.write(i)

def hm7(): # hm7
  hm7 = str(input('Введите текст: '))
  with open('hm8_8.txt', 'w', encoding='utf-8') as example_1, open('hm8_8.txt', 'a', encoding='utf-8') as example_2:
    example_1.write(f'{hm7}\n ')
    example_2.write(f'{hm7}\n ')
    print(f'файл {hm7} сохранён')

hm7()