from db_untils import connect, close_connection
import psycopg2

def get_columns(column_name):
    conn = None

    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * from {}".format(column_name))

        rows = cur.fetchall()

        cur.close()
        return rows

    except (Exception, psycopg2.DatabaseError) as error:
        print(">>>ERROR: ", error)

    finally:
        close_connection(conn)

def get_student(student_name, student_id, class_name):
   
    
    conn = None

    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
                        SELECT * 
                        FROM student, class1
                        WHERE student_name LIKE '%""" + student_name + """%' 
                            AND student_id = '""" + student_id + """' 
                            AND class_name = '""" + class_name + """'
                    """)
        
        result = cur.fetchall()
        cur.close()

        return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        close_connection(conn)