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
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             TYPE      TEXT    NOT NULL,
             AGE       INT     NOT NULL,
             RACE      TEXT    NOT NULL,
             SEX       TEXT    NOT NULL,
             PRICE     REAL);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS CLIENTS
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 PASSWORD  TEXT          NOT NULL,
                 EMAIL     TEXT          NOT NULL);''')
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

def verify_sign_in(conn, email ):
    cur=conn.cursor()
    data=cur.execute("SELECT * FROM CLIENTS WHERE EMAIL = \"{}\" ".format(email)).fetchall()
    if len(data)==0:
        return True
    return False

def insert_in_clients(conn, email, password):
    sql_to_insert="INSERT INTO CLIENTS (PASSWORD, EMAIL) VALUES (\"{}\",\"{}\")".format(password, email)
    cur=conn.cursor()
    cur.execute(sql_to_insert)
    conn.commit()

def verify_log_in(conn, email, password):
    cur = conn.cursor()
    data = cur.execute("SELECT * FROM CLIENTS WHERE EMAIL = \"{}\" AND PASSWORD = \"{}\"".format(email, password)).fetchall()
    if len(data)!=0:
        return True
    return False

def delete_by_id(conn, id):
    sql = 'DELETE FROM PETSHOP WHERE ID=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()