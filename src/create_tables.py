import psycopg2
from db_untils import execute_commands

commands = (
        """
        CREATE TABLE subject(
            subject_id CHAR(3) PRIMARY KEY NOT NULL,
	        subject_name VARCHAR(30) NOT NULL,
	        units INT
        )
        """,

        """
        CREATE TABLE class1(
            class_id CHAR(3) PRIMARY KEY NOT NULL,
            class_name VARCHAR(30) NOT NULL,
            class_year CHAR(9)   
        )
        """,

        """
        CREATE TABLE student(
            student_id CHAR(5) NOT NULL,
            student_name VARCHAR(30) NOT NULL,
            student_address VARCHAR(30),
            class_id CHAR(3) NOT NULL,
            PRIMARY KEY (student_id, class_id)
        )
        """,

        """
        CREATE TABLE student_grades(
            student_id CHAR(5),
            subject_id CHAR(3),
            grades REAL,
            PRIMARY KEY (student_id, subject_id)
        )
        """
)

if __name__ == '__main__':
    execute_commands(commands)