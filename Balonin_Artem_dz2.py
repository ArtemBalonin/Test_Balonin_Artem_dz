# Задание №2: Создать список, состоящий из кубов нечетных чисел от 1 до 1000
#             а) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится на 7
#             б) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр
#     которых делится нацело на 7
#             в) решить задачу под пунктом б, не создавая новый список

cubes = [x**3 for x in range (1000) if x%2 != 0]
print('Создан список кубов нечетных чисел{}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list = []
for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    for i in range(len(my_list)):
        my_numbers_sum = my_numbers_sum + my_list[i]
    if my_numbers_sum % 7 ==0:
        # print('Сумму чисел, делящихся на 7:', my_numbers_sum)
        my_numbers_sum_list.append(my_numbers_sum)
print('Список чисел, делящихся на 7:', my_numbers_sum_list)
input = 17
cubes1 = []
my_numbers_sum1 = 0
my_numbers_sum_list1 = []
for nums in cubes:
    number = nums + input
    cubes1.append(number)
print('Список чисел, после прибавления к каждому значению 17:', cubes1)
for i in range(len(cubes1)):
    my_str1 = str(cubes1[i])
    my_list1 = list(my_str1)
    for i in range(len(my_list1)):
        my_list1[i] = int(my_list1[i])
    for i in range(len(my_list1)):
        my_numbers_sum1 = my_numbers_sum1 + my_list1[i]
    if my_numbers_sum1 % 7 == 0:
        # print('Сумма чисел, делящтхся на 7: ', my_numbers_sum1)
        my_numbers_sum_list1.append(my_numbers_sum1)
print('Список чисел, делящихся на 7:', my_numbers_sum_list1)