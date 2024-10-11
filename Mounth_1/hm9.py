# data_1 = {1,3,5,3.14,3,51.123,5,3.14,1,6,-1}
# print(type(data_1)) #hm1
# data_2 = {4,1,6,1,3.14,5.13,6,4}
# result_1 = sum(data_1)
# result_2 = sum(data_2)
# print(f'{result_1} + {result_2} = {result_1 + result_2}') #hm2
#
#
# def intersection(set1, set2): #hm3
#     return set(set1) & set(set2)
#
# new_1 = (3.14, 3, 14, 5, 9, 1)
# new_2 = (3, 15, 3, 2, 3.14, 5, 7, 1)
#
# print(intersection(new_1,new_2))


# data_origin = [3,1,5,1,3,5,4,13,12,6,4,5]
# def for_set(): #hm4
#     data_set = set(data_origin)
#     data_list = list(data_set)
#     print(type(data_list), data_list)
#
# for_set()

# def is_subset(set1, set2): # hm5
#     return set1.issubset(set2)
# a = {1, 2, 3}
# b = {1, 2, 3, 4, 5}
#
# print(is_subset(a, b))


def calculator():
    try:
        numb_1 = float(input('Введите первое число: '))
        choice = str(input('Введите знак "+", "-", "*" "/"\nВвести знак: '))
        numb_2 = float(input('Введите второе число: '))
        if choice == '+':
            plus = numb_1 + numb_2
            if plus % 2 == 0:
                return f'{plus} чётное число'
            else:
                return f'{plus} нечётное число'
        elif choice == '-':
            minus = numb_1 - numb_2
            if minus % 2 == 0:
                return f'{minus} чётное число'
            else:
                return f'{minus} нечётное число'
        elif choice == '*':
            multiplication = numb_1 * numb_2
            if multiplication % 2 == 0:
                return f'{multiplication} чётное число'
            else:
                return f'{multiplication} нечётное число'
        elif choice == '/':
            division = numb_1 / numb_2
            if division % 2 == 0:
                return f'{division} чётное число'
            else:
                return f'{division} нечётное число'
    except ZeroDivisionError:
        return 'Вы пытались разделить на ноль ошибка'
    except ValueError:
        return 'Ошибка синтаксиса попробуйте ввести числа'
print(calculator())
print(calculator())
print(calculator())
print(calculator())