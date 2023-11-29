import mysql.connector
from tabulate import tabulate

#connection_String
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mathan123",
    database="lms"
)

def create_student(name,age,department,eligible):
    try:
        cursor = connection.cursor()
        statement = "insert into student (name,age,department,eligible) values('{}',{},'{}',{})".format(
            name, age, department, eligible)
        cursor.execute(statement)
        connection.commit()
        print("Student {} created".format(name))
    except Exception as e:
        print("Student Not created")

def update_student(rollno,name,age,department,eligible):
    try:
        cursor = connection.cursor()
        statement = "update student set name = '{}', age = {}, department = '{}', eligible = {} where rollno = {}".format(name, age, department, eligible,rollno)
        cursor.execute(statement)
        connection.commit()
        print( "Student '{}' Updated!".format(name))

    except Exception as e:
        print("Student '{}' not Updated!".format(name))

def delete_student(rollno):
    try:
        cursor = connection.cursor()
        statement = "select * from student where rollno = {}".format(int(rollno))
        cursor.execute(statement)
        student = cursor.fetchone()
        if student:
            statement = "delete from student where rollno = {}".format(int(rollno))
            cursor.execute(statement)
            connection.commit()
            print( "Student {} deleted!".format(rollno))
        else:
            print( "Student {} not deleted!".format(rollno))
    except Exception as e:
        return e



def view_student(rollno):
    try:
        cursor = connection.cursor()
        if int(rollno) == -1:
            statement = "select * from student"
            cursor.execute(statement)
            rows = cursor.fetchall()
            print(tabulate(rows, headers=['roll_no', 'name', 'age', 'department', 'eligible']))
        else:
            statement = "select * from student where rollno = {}".format(int(rollno))
            cursor.execute(statement)
            student = cursor.fetchall()
            if student:
                print(tabulate(student, headers=['roll_no', 'name', 'age', 'department', 'eligible']))
            else:
                print("Student not found")
    except Exception as e:
        print("Something went wrong")

choice = True

while choice:
    print("1.create student")
    print("2.update student")
    print("3.delete student")
    print("4.view student")
    print("5.exit")

    ch=int(input("Enter your choice:"))

    if ch==1:
        name = input('enter the name:')
        age = int(input("enter the age:"))
        department = input("enter the department:")
        eligible = int(input("enter eligible:"))
        create_student(name,age,department,eligible)
    elif ch==2:
        view_student(-1)
        rollno = int(input("enter the rollno"))
        name = input('enter the name:')
        age = int(input("enter the age:"))
        department = input("enter the department:")
        eligible = int(input("enter eligible:"))
        update_student(rollno,name,age,department,eligible)
        view_student(-1)
    elif ch==3:
        view_student(-1)
        rollno = int(input("enter the rollno"))
        delete_student(rollno)
        view_student(-1)
    elif ch==4:
        view_student(-1)
    elif  ch==5:
        print("Thank You...")
        exit()
    else:
        print("Incorrect Choice")





