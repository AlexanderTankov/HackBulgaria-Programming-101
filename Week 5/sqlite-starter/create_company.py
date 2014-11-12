import sqlite3


def insert_in_db_file(name, monthly_salary, yearly_bonus, position):
    db = sqlite3.connect('create_company.db')

    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE if not exists users(id INTEGER PRIMARY KEY, name TEXT,
                           monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
    ''')
    cursor.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position)
                      VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))
    db.commit()
    db.close()

if __name__ == '__main__':

    insert_in_db_file("Ivan Ivanov", 5000, 10000, "Software Developer")
    insert_in_db_file("Rado Rado", 500, 0, "Technical Support Intern")
    insert_in_db_file("Ivo Ivo", 10000, 100000, "CEO")
    insert_in_db_file("Petar Petrov", 3000, 1000, "Marketing Manager")
    insert_in_db_file("Maria Georgieva", 8000, 10000, "COO")
