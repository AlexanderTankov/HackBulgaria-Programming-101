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


def show_num_of_free_spots(projection_id):
    all_reservations = cursor.execute('''SELECT * FROM reservations WHERE projection_id = ?''', (projection_id,))
    employed_spots = 0
    for reservation in all_reservations:
        employed_spots += 1
    return (100 - employed_spots)


def show_movie_projections(movie_id, date=""):
    all_movies = cursor.execute('''SELECT * FROM movies''')
    for movie in all_movies:
        if movie["id"] == movie_id:
            print("Projections for movie: {}".format(movie["name"]))

    all_projections = cursor.execute('''SELECT * FROM projections ORDER BY date || time''').fetchall()
    for projection in all_projections:
        i = 1
        if projection["movie_id"] == movie_id and date == "":
            print("[{}] - {} {} ({}) - {} spots available".format(projection["id"], projection["date"], projection["time"], projection["type"], show_num_of_free_spots(projection['id'])))
        elif projection["movie_id"] == movie_id:
            print("[{}] - {} ({}) - {} spots available".format(i, projection["time"], projection["type"], show_num_of_free_spots(projection['id'])))
            i += 1


def get_list_of_spots(projection_id):
    result = []
    employed_spots = cursor.execute('''SELECT * FROM reservations WHERE projection_id = ?''', (projection_id,)).fetchall()
    for spots in employed_spots:
        result.append((spots["row"], spots["col"]))
    return result


def show(row, col=""):
    if col == "":
        return "{}  . . . . . . . . . .".format(row)
    else:
        i = 0
        if(row == 10):
            result = "{}".format(row)
        else:
            result = "{} ".format(row)

        for x in range(1, 11):
            if i < len(col) and x == col[i]:
                result += " X"
                i += 1
            else:
                result += " ."
    return result


def make_reservation():
    client_name = input("Step 1 (User): Choose name> ")
    client_num_of_tickets = input("Step 1 (User): Choose number of tickets> ")
    show_movies()
    movie_choice = input("Step 2 (Movie): Choose a movie> ")
    show_movie_projections(int(movie_choice))
    projection_choice = input("Step 3 (Projection): Choose a projection> ")
    print("Available seats (marked with a dot):")
    employed_spots = sorted(get_list_of_spots(int(projection_choice)))
    print("   1 2 3 4 5 6 7 8 9 10")
    for x in range(1, 11):
        temp = []
        for elem in employed_spots:
            if elem[0] == x:
                temp.append(elem[1])
        print(show(x, temp))

    reservation_seat = []
    for x in range(0, int(client_num_of_tickets)):
        seat_choice = input("Step 4 (Seats): Choose seat {}> ".format(x + 1))
        reservation_seat.append((seat_choice[1], seat_choice[3]))

    print("This is your reservation:")
    all_movies = cursor.execute('''SELECT * FROM movies''')
    for movie in all_movies:
        if movie["id"] == int(movie_choice):
            print("Movie: {}".format(movie["name"]))

    all_projections = cursor.execute('''SELECT * FROM projections ORDER BY date || time''').fetchall()
    for projection in all_projections:
        if projection["id"] == int(projection_choice):
            print("{} {} ({})".format(projection["date"], projection["time"], projection["type"]))

    moment_res = "Status: "
    for x in range(0, len(reservation_seat)):
            moment_res += "{} ".format(reservation_seat[x])
    print(moment_res)

    final = input("Step 5 (Confirm - type 'finalize')> ")
    if final == "finalize":
        print("thanks")
    else:
        print("wrong")

    for x in range(0, int(client_num_of_tickets)):

        insert_in_reservations_db_file(client_name, int(projection_choice), reservation_seat[x][0], reservation_seat[x][1])



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

    make_reservation()
    con.commit()
    con.close()
