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


def insert_in_reservations_db_file(username, projection_id, row, col):
    db = sqlite3.connect('cinema_database.db')

    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE if not exists reservations(id INTEGER PRIMARY KEY, username TEXT,
                           projection_id INTEGER, row INTEGER, col INTEGER)
    ''')
    cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                      VALUES(?,?,?,?)''', (username, projection_id, row, col))

    db.commit()
    db.close()


def show_movies():
    print("Current movies:")
    all_movies = cursor.execute('''SELECT * FROM movies ORDER BY rating desc''')
    for movie in all_movies:
        print("[{}]: {} - {}".format(movie["id"], movie["name"], movie["rating"]))


def show_movie_projections(movie_id, date=""):
    all_movies = cursor.execute('''SELECT * FROM movies''')
    for movie in all_movies:
        if movie["id"] == movie_id:
            print("Projections for movie: {}".format(movie["name"]))

    all_projections = cursor.execute('''SELECT * FROM projections ORDER BY date || time''')
    for projection in all_projections:
        i = 0
        if projection["movie_id"] == movie_id and date == "":
            print("[{}] - {} {} ({})".format(projection["id"], projection["date"], projection["time"], projection["type"]))
        elif projection["movie_id"] == movie_id:
            print("[{}] - {} ({})".format(i, projection["time"], projection["type"]))
            i += 1


def make_reservation():
    pass

if __name__ == '__main__':
    con = sqlite3.connect('cinema_database.db')
    con.row_factory = sqlite3.Row

    cursor = con.cursor()

    # insert_in_movies_db_file("The Hunger Games: Catching Fire", 7.9)
    # insert_in_movies_db_file("Wreck-It Ralph", 7.8)
    # insert_in_movies_db_file("Her", 8.3)

    # insert_in_projections_db_file(1, "3D", "2014-04-01", "19:10")
    # insert_in_projections_db_file(1, "2D", "2014-04-01", "19:00")
    # insert_in_projections_db_file(1, "4DX", "2014-04-02", "21:00")
    # insert_in_projections_db_file(3, "2D", "2014-04-05", "20:20")
    # insert_in_projections_db_file(2, "3D", "2014-04-02", "22:00")
    # insert_in_projections_db_file(2, "2D", "2014-04-02", "19:30")

    # insert_in_reservations_db_file("RadoRado", 1, 2, 1)
    # insert_in_reservations_db_file("RadoRado", 1, 3, 5)
    # insert_in_reservations_db_file("RadoRado", 1, 7, 8)
    # insert_in_reservations_db_file("Ivo", 3, 1, 1)
    # insert_in_reservations_db_file("Ivo", 3, 1, 2)
    # insert_in_reservations_db_file("Mysterious", 5, 2, 3)
    # insert_in_reservations_db_file("Mysterious", 5, 2, 4)

    show_movies()
    show_movie_projections(2)
    show_movie_projections(1, "2014-04-01")
    con.commit()
    con.close()
