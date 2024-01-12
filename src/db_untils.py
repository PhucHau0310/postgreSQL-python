from config import config
import psycopg2

def connect():
    conn = None
    try:
        params = config()
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)
        return conn
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(">>>ERROR: ", error)

def close_connection(conn):
    if conn is not None:
        conn.close()
        print('Database connection closed.')

def execute_commands(commands):
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)

        cur.close()
        conn.commit()

        print('Commands executed successfully !')
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(">>>ERROR: ", error)

    finally:
        close_connection(conn)


def insert_data(table_name, data_list, columns):

    sql = f"INSERT INTO {table_name}({', '.join(columns)}) VALUES({', '.join(['%s']*len(columns))})"
    
    print(sql)
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        for data in data_list:
            cur.execute(sql, data)

        conn.commit()

        print('Insert data successfully!')
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(">>>ERROR: ", error)

    finally:
        if conn is not None:
            conn.close()