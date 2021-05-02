import json
import random
import re

"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def task1():
    print("Task 1")
    file_name = input("Введите название файла:")
    with open(f"{file_name}.txt", 'w') as file_txt:
        while True:
            text_line = input("Введите строку для записи в файл (ENTER - конец):")
            if text_line == "":
                break
            file_txt.write(f'{text_line}\n')


'''
2. Создать текстовый файл(не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
'''


def task2():
    print("Task 2")
    with open("text.txt", "r") as file_txt:
        row = 0
        for text_line in file_txt:
            row += 1
            l = re.split(r'\s+', text_line)
            print(f'В {row} строке  слов: {len(l)}')
        print(f"Всего строк в файле: {row}")


'''
3. Создать текстовый файл (не программно), 
построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
'''


def task3():
    print("Task 3")
    with open("fio.txt", "r",  encoding="utf-8") as file_txt:
        sum = 0
        n = 0
        for text_line in file_txt:
            l = re.split(r'\s+', text_line)
            sum = sum + int(l[3])
            n += 1
            if int(l[3]) < 20000:
                print(f"Сотрудник по фамилии {l[0]} имеет оклад ниже 20000, а именно: {l[3]}")
        average = sum / n
        print(f"Средняя величина дохода сотрудников составляет: {average}")


'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
'''


def task4():
    print("Task 4")
    d = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    with open("numbers.txt", "r") as file_txt:
        with (open("numbers_out.txt", "w", encoding="utf-8")) as file_out:
            for text_line in file_txt:
                l = text_line.split('-')
                file_out.write(f'{d[l[0]]}-{l[1]}')


'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле 
и выводить ее на экран.
'''


def task5():
    print("Task 5")
    # Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    with (open("numbers_out2.txt", "w")) as file_out:
        file_out.write(" ".join(map(str, [random.randint(0, 20) for i in range(30)])))
    # Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
    with (open("numbers_out2.txt", "r")) as f:
        print(f"Сумма чисел в файле number_out2.txt составляет: {sum([int(item) for item in f.read().split()])}")


'''
6. Необходимо создать (не программно) текстовый файл, 
где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
'''


def task6():
    with (open("studies.txt", "r", encoding="utf-8")) as file:
        d = dict()
        for s in file:
            subject_name = s.split(':')[0]
            hours = re.findall(r"[-+]?\d+", s)
            sum_hours = sum([int(item) for item in hours])
            print(f'{subject_name}: {sum_hours}')
            d[subject_name] = sum_hours
        print(d)


def task7():
    # Ввод данных из файла в массив
    with open('firms.txt', 'r', encoding="utf-8") as file:
        lst = file.readlines()
    rows = len(lst)
    lst = [[n for n in x.split()] for x in lst]
    print(lst)
    # расчет прибылей
    earnings = [float(lst[j][2]) - float(lst[j][3]) for j in range(rows)]
    # расчет средней прибыли
    sum_earnings = 0
    count_earnings = 0
    for item in earnings:
        if item > 0:
            sum_earnings += item
            count_earnings += 1
    average = sum_earnings / count_earnings
    print(f"Средняя прибыль: {average}")
    d_earnings = dict()
    for i in range(rows):
        d_earnings[lst[i][0]] = earnings[i]
    print(f'd = {d_earnings}')
    d_average = dict()
    d_average["average_profit"] = average
    l_out = list()
    l_out.append(d_earnings)
    l_out.append(d_average)
    print(l_out)
    # [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]
    with (open("json.json", "w")) as file:
        json.dump(l_out, file)


task1()
task2()
task3()
task4()
task5()
task6()
task7()
