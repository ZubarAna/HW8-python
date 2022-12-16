from view import *
from models import *

def menu():
    con = create_db()
    while True:
        user_choice = inp_menu()
        if user_choice == '1':
            add_w = add_worker()
            data_add = insert_employer(add_w, con)
            print_data(data_add)
        elif user_choice == '2':
            p_all = print_all(con)
            print_data(p_all)
        elif user_choice == '3':
            find_w = find_worker()
            slm = select_last_name(con, find_w)
            print_data(slm)
        elif user_choice == '4':
            find_pos = find_position()
            sel_pos = select_position(con, find_pos)
            print_data(sel_pos)
        elif user_choice == '5':
            p_all = print_all(con)
            print_data(p_all)
            change_zp = change_salary()
            ch_sal = change_sal(con, *change_zp)
            print_data(ch_sal)
        elif user_choice == '6':
            d_zp = data_zp(con)
            print_data(d_zp)
        elif user_choice == '7':
            p_all = print_all(con)
            print_data(p_all)
            delete_work = delete_worker()
            del_emp = delete_emp(con, *delete_work)
            print(del_emp)
        elif user_choice == '0':
            print('До свидания')
            break
        else:
            print('Вы что-то напутали с вводом')
