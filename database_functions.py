import sqlite3
def connection():
    conn = sqlite3.connect('animals.db')
    if conn==None:
        return None
    else:
        return conn

def create_table():
    conn=connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS PETSHOP
             (ID INT PRIMARY KEY     NOT NULL,
             TYPE      TEXT    NOT NULL,
             AGE       INT     NOT NULL,
             RACE      TEXT    NOT NULL,
             SEX       TEXT    NOT NULL,
             PRICE     REAL);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS CLIENTS
                 (ID INT PRIMARY KEY     NOT NULL,
                 GENDER      TEXT    NOT NULL,
                 AGE       INT     NOT NULL,
                 NAME      TEXT    NOT NULL,
                 EMAIL     TEXT    NOT NULL);''')
    cursor=conn.cursor()
    sqlite_insert_query = """INSERT INTO PETSHOP
                          (ID, TYPE, AGE, RACE, SEX, PRICE) 
                           VALUES 
                          (1,'Pisica',1, 'birmaneza', 'feminin',700)"""

    sqlite_insert_query_2 = """INSERT INTO PETSHOP
                           (ID, TYPE, AGE, RACE, SEX, PRICE) 
                            VALUES 
                           (2,'Caine',2, 'husky', 'masculin',1000)"""

    count = cursor.execute(sqlite_insert_query)
    count = cursor.execute(sqlite_insert_query_2)
    conn.commit()
    conn.close()

def get_all_animals(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM PETSHOP;")

    rows = cur.fetchall()
    return rows
