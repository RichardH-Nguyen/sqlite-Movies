import sqlite3

sqlite_file = 'movie_db.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
print('Opened database Successfully')


def CreateMovieTable():
    c.execute('''CREATE TABLE IF NOT EXISTS MOVIES
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL, 
    LENGTH INT, 
    DIRECTOR TEXT,
    WRITER TEXT, 
    LEADROLE TEXT, 
    RELEASEDATE DATE);''')

    print('Table created successfully')

    conn.commit()


def AddNewRow(Name, length, director, writer, lead, releaseDate):
    # Add new row
    sql = '''INSERT INTO MOVIES (NAME, LENGTH, DIRECTOR, WRITER, LEADROLE, RELEASEDATE )\
              VALUES (?, ?, ?, ?, ?, ?)'''

    c.execute(sql, (Name, length, director, writer, lead, releaseDate))

    conn.commit()

def UpdateRow(column, newValue, id):
    # Specified row
    sql ='''UPDATE MOVIES 
    SET %s = ? 
    WHERE ID = ?'''

    c.execute(sql % (column,), (newValue, id))

    conn.commit()

def DeleteRow(id):
    # Deletes row by id number
    sql = '''DELETE FROM MOVIES WHERE ID=?'''

    c.execute(sql, (id,))

    conn.commit()

def DisplayTable():
    # Displays entire table
    cursor = c.execute("SELECT * FROM MOVIES")

    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("LENGTH = ", row[2])
        print("DIRECTOR = ", row[3])
        print("WRITER = ", row[4])
        print("LEAD ROLE = ", row[5])
        print("RELEASE DATE = ", row[6])
        print('\n============================\n')

def DisplaySingleRow(id):
    # Displays a single row by id
    sql = '''SELECT * FROM MOVIES WHERE ID = ?'''

    cur = c.execute(sql, (id,))

    for row in cur:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("LENGTH = ", row[2])
        print("DIRECTOR = ", row[3])
        print("WRITER = ", row[4])
        print("LEAD ROLE = ", row[5])
        print("RELEASE DATE = ", row[6])

def CloseDatabase():
    c.close()