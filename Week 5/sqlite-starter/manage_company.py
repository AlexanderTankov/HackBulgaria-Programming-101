import sqlite3
from create_company import insert_in_db_file


def list_employees():
    all_rows = cursor.execute('''SELECT id, name, position FROM users''')
    all_rows = cursor.fetchall()

    for row in all_rows:
        print("{}: {} - {}".format(row["id"], row["name"], row["position"]))


def monthly_spending():
    cursor.execute('''SELECT SUM(monthly_salary) AS totalsum FROM users''')
    result = cursor.fetchone()
    return result["totalsum"]


def yearly_spending():
    monthly = monthly_spending()
    cursor.execute('''SELECT SUM(yearly_bonus) AS totalsum FROM users''')
    result = cursor.fetchone()
    return result["totalsum"] + monthly * 12


def delete_employee(employee_id):
    cursor.execute('''DELETE FROM users WHERE id = ? ''', (employee_id,))


def add_employee(name, monthly_salary, yearly_bonus, position):
    insert_in_db_file(name, monthly_salary, yearly_bonus, position)

if __name__ == '__main__':
    con = sqlite3.connect('create_company.db')
    con.row_factory = sqlite3.Row

    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE if not exists users(id INTEGER PRIMARY KEY, name TEXT,
                           monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
    ''')

    list_employees()
    print(monthly_spending())
    print(yearly_spending())
    list_employees()

    con.commit()

    con.close()
