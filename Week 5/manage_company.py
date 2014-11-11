import sqlite3


def list_employees():
    all_rows = cursor.execute('''SELECT name, position FROM users''')
    all_rows = cursor.fetchall()

    for row in all_rows:
        print("{} - {}".format(row["name"], row["position"]))


def monthly_spending():
    cursor.execute('''SELECT SUM(monthly_salary) AS totalsum FROM users''')
    result = cursor.fetchone()
    print(result["totalsum"])

if __name__ == '__main__':
    con = sqlite3.connect('create_company.db')
    con.row_factory = sqlite3.Row

    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE if not exists users(id INTEGER PRIMARY KEY, name TEXT,
                           monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
    ''')
    con.commit()

    list_employees()
    monthly_spending()

    con.close()
