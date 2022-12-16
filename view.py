def inp_menu():
    inp_choice = input('''Чего изволите?
# 1 добавление сотрудника
# 2 посмотреть всех сотрудников
# 3 найти сотрудника по фамилии
# 4 найти по должности
# 5 изменить зарплату
# 6 общий фонд з/п
# 7 удаление сотрудника
# 0 выход

''')
    return inp_choice


def add_worker():
    print(f'''Введите данные добавляемого сотрудника через  
    id name last_name position salary bonus''')
    inp_name = input("Введите имя: ").capitalize()
    inp_last_name = input("Введите фамилию: ").capitalize()
    inp_position = input("Введите должность: ").capitalize()
    inp_salary = int(input("Введите заработную плату: "))
    inp_bonus = int(input("Введите премию: "))
    return inp_name, inp_last_name, inp_position, inp_salary, inp_bonus


def find_worker():
    worker = input('Введите фамилию сотрудника, которого хотите найти: ')
    return worker


def find_position():
    position = input('Введите должность: ')
    return position

def change_salary():
    id_worker = input('Введите id сотрудника, которого хотите найти: ')
    new_salary = int(input('Введите новую заработную плату: '))
    return id_worker, new_salary


def print_data(inp_str):
    print(inp_str)


def delete_worker():
    id_worker = input('Введите id сотрудника, которого хотите удалить: ')
    return id_worker