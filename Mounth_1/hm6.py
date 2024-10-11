# def is_even(a): #hm1
#   if a % 2 == 0:
#     print(f'{a} True')
#   else:
#     print(f'{a} False')
# is_even(int(input('Введите число: ')))

# def factorial(n): #hm2
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# print(factorial(9))


# def list_py(): #hm3
#   my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   list_two = []
#   for i in my_list:
#     if i % 2 == 0:
#       print(f'{i} чётное число',end = ' ')
#       list_two.append(i)
#     else:
#       pass

# list_py()

# def hm4(): # hm4
#   text = str(input('Введите текст: '))
#   hm4 = text[::-1]
#   print(hm4)

# hm4()

# def hm5(words): #hm5
#   for word in words:
#     if word == word[::-1]:
#       print(word)
#     else:
#       print('Ошибка')

# words = ["azat", "madam", "sema", "anna", "kazak", "aktan", "zakaz"]
# hm5(words)