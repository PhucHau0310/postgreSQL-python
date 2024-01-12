from insert_data import insert_subject, insert_class, insert_student, insert_student_grades
from db_untils import connect, close_connection
from queries import get_columns, get_student
import random
import tkinter as tk
from tkinter import ttk

data_insert = {
    'subject': [
        ('S01','Math',3),
        ('S02','Physics',3),
        ('S03','Chemistry',3),
        ('S04','Literature',2),
        ('S05','Biology',2)
    ],
    "class1": [
        ('C01', 'Class A', '2023'),
        ('C02', 'Class B', '2023'),
        ('C03', 'Class C', '2023'),
        ('C04', 'Class D', '2023'),
        ('C05', 'Class E', '2023'),
        ('C06', 'Class F', '2023'),    
    ],
    "students": [
        ('STU01', 'Student 1', 'Address 1', 'C01'),
        ('STU02', 'Student 2', 'Address 2', 'C01'),
        ('STU03', 'Student 3', 'Address 3', 'C02'),
        ('STU04', 'Student 4', 'Address 4', 'C02'),
        ('STU05', 'Student 5', 'Address 5', 'C03'),
        ('STU06', 'Student 6', 'Address 6', 'C03'),
        ('STU07', 'Student 7', 'Address 7', 'C04'),
        ('STU08', 'Student 8', 'Address 8', 'C04'),
        ('STU09', 'Student 9', 'Address 9', 'C05'),
        ('STU10', 'Student 10', 'Address 10', 'C05'),        
    ],
    "student_grades": []
}

for student_id in ['STU01', 'STU02', 'STU03', 'STU04', 'STU05', 'STU06', 'STU07', 'STU08', 'STU09', 'STU10']:
    for subject_id in ['S01', 'S02', 'S03', 'S04', 'S05']:
        data_insert['student_grades'].append((student_id, subject_id, round(random.uniform(1.0, 10.0), 2)))

def add_student():
    print("add student")

def search_student():
    print("Search student")

def update_student():
    print("Update student")

def delete_student():
    print("Delete student")


def submit():
    name = name_entry.get() 
    student_id = student_id_entry.get()
    class_name = class_combobox.get()

    student_list.delete(0, tk.END)
    
    result = get_student(name, student_id, class_name)

    # student_list.insert(tk.END, name + " - " + student_id + " - " + class_name)

    for item in result[0]:
        if ('STU' in item):
            student_list.insert(tk.END, "Student ID: {}".format(item))
        elif ('Student' in item):
            student_list.insert(tk.END, "Student Name: {}".format(item))
        elif ('Address' in item):
            student_list.insert(tk.END, "Address: {}".format(item))
        elif ('C0' in item):
            student_list.insert(tk.END, "Class ID: {}".format(item))
        elif ('20' in item):
            student_list.insert(tk.END, "School Year: {}".format(item))

if __name__ == '__main__':
    conn = connect()

    # insert_subject(data_insert['subject'])
    # insert_class(data_insert['class1'])
    # insert_student(data_insert['students'])
    # insert_student_grades(data_insert['student_grades'])

    # students = get_columns("student")
    # students_grades = get_columns("student_grades")
    # class1s = get_columns("class1")
    # subjects = get_columns("subject")

    # for student in class1s:
    #     print(student)

    root =  tk.Tk()
    root.title("Student Management System")

    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Add new student", command=add_student)
    file_menu.add_command(label="Search student", command=search_student) 
    file_menu.add_command(label="Update student", command=update_student)
    file_menu.add_command(label="Delete student", command=delete_student)

    menu_bar.add_cascade(label="Student", menu=file_menu) 
    root.config(menu=menu_bar)

    input_frame = ttk.LabelFrame(root, text="Input")
    input_frame.grid(row=0, column=0, padx=20, pady=20)

    name_label = ttk.Label(input_frame, text="Name:")
    name_entry = ttk.Entry(input_frame)

    student_id_label = ttk.Label(input_frame, text="Student ID:") 
    student_id_entry = ttk.Entry(input_frame)

    class_label = ttk.Label(input_frame, text="Class:")
    class_combobox = ttk.Combobox(input_frame) 
    classes = ["Class A", "Class B", "Class C", "Class D", "Class E", "Class F"]
    class_combobox['values'] = classes
    class_combobox.current(0)

    submit_button = ttk.Button(input_frame, text="Submit", command=submit)

    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry.grid(row=0, column=1, padx=10, pady=10)  

    student_id_label.grid(row=1, column=0, padx=10, pady=10)
    student_id_entry.grid(row=1, column=1, padx=10, pady=10)   

    class_label.grid(row=2, column=0, padx=10, pady=10)  
    class_combobox.grid(row=2, column=1, padx=10, pady=10)

    submit_button.grid(row=3, column=1, padx=10, pady=10)

    student_list = tk.Listbox(root, height=15, width=60)
    student_list.grid(row=1, column=0, padx=20, pady=20)

   
    root.mainloop()

    close_connection(conn)