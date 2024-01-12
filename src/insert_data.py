import psycopg2
from db_untils import insert_data

def insert_subject(subject_list):
    columns = ['subject_id', 'subject_name', 'units']
    insert_data('subject', subject_list, columns)

def insert_class(class_list):
    columns = ['class_id', 'class_name', 'class_year']
    insert_data('class1', class_list, columns)

def insert_student(student_list):
    columns = ['student_id', 'student_name', 'student_address', 'class_id']
    insert_data('student', student_list, columns)

def insert_student_grades(student_grades_list):
    columns = ['student_id', 'subject_id', 'grades']
    insert_data('student_grades', student_grades_list, columns)