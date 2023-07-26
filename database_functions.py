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
             PRICE     REAL);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS CLIENTS
                 (ID INT PRIMARY KEY     NOT NULL,
                 GENDER      TEXT    NOT NULL,
                 AGE       INT     NOT NULL,
                 NAME      TEXT    NOT NULL,
                 EMAIL     TEXT    NOT NULL);''')
    conn.close()