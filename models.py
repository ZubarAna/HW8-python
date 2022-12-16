import sqlite3


def create_db():
    con = sqlite3.connect('staff.db')
    cur = con.cursor()
    query = '''CREATE TABLE IF NOT EXISTS
    staff(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INTEGER,
    bonus INTEGER);
    '''
    cur.execute(query)
    con.commit()
    return con


def insert_employer(new_data: tuple, con):
    print(new_data)
    print(con)
    cur = con.cursor()
    cur.execute(
        'INSERT INTO staff (name, last_name, position, salary, bonus) VALUES(?,?,?,?,?)', new_data)
    con.commit()
    return 'Данные добавлены'


def print_all(con):
    cur = con.cursor()
    res_all = cur.execute('SELECT * FROM staff;')
    res = res_all.fetchall()
    out_str = ''
    for i in res:
        out_str += ' '.join(map(str, i))
        out_str += '\n'
    return out_str


def data_zp(con):
    cur = con.cursor()
    res = cur.execute('SELECT salary, bonus FROM staff').fetchall()
    out_int = 0
    for i in res:
        out_int += sum(i)
    return out_int


def select_last_name(con, last_name):
    cur = con.cursor()
    res = cur.execute(
        f'SELECT * FROM staff WHERE last_name LIKE "{last_name.capitalize()}%";').fetchall()
    out_str = ''
    for i in res:
        out_str += ' '.join(map(str, i))
        out_str += '\n'
    return out_str


def select_position(con, pos):
    cur = con.cursor()
    res = cur.execute(
        f'SELECT * FROM staff WHERE position LIKE "{pos.capitalize()}%";').fetchall()
    out_str = ''
    for i in res:
        out_str += ' '.join(map(str, i))
        out_str += '\n'
    return out_str


def change_sal(con, id_str, zp_str):
    cur = con.cursor()
    cur.execute(f"UPDATE staff SET salary = {zp_str} WHERE id = {id_str}")
    con.commit()
    return f'Изменили заработную плату'
