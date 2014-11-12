import sqlite3


def insert_in_movies_db_file(name, rating):
    db = sqlite3.connect('cinema_database.db')

    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE if not exists movies(id INTEGER PRIMARY KEY, name TEXT,
                           rating INTEGER)
    ''')
    cursor.execute('''INSERT INTO movies(name, rating)
                      VALUES(?,?)''', (name, rating))

    db.commit()
    db.close()


def insert_in_projections_db_file(movie_id, type_of_movie, date_of_movie, time):
    db = sqlite3.connect('cinema_database.db')

    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE if not exists projections(id INTEGER PRIMARY KEY, movie_id INTEGER
                           type TEXT, date TEXT, time TEXT)
    ''')
    cursor.execute('''INSERT INTO projections(movie_id, type, date, time)
                      VALUES(?,?,?,?)''', (movie_id, type_of_movie, date_of_movie, time))

    db.commit()
    db.close()


if __name__ == '__main__':
    insert_in_movies_db_file("The Hunger Games: Catching Fire", 7.9)
    insert_in_movies_db_file("Wreck-It Ralph", 7.8)
    insert_in_movies_db_file("Her", 8.3)

    insert_in_projections_db_file(1, "3D", "2014-04-01", "19:10")
    insert_in_projections_db_file(1, "2D", "2014-04-01", "19:00")
    insert_in_projections_db_file(1, "4DX", "2014-04-02", "21:00")
    insert_in_projections_db_file(3, "2D", "2014-04-05", "20:20")
    insert_in_projections_db_file(2, "3D", "2014-04-02", "22:00")
    insert_in_projections_db_file(2, "2D", "2014-04-02", "19:30")
