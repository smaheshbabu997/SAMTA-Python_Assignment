import mysql.connector

def create_database(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS school")
    cursor.execute("USE school")

def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            age INT,
            grade FLOAT
        )
    """)

def insert_record(cursor, first_name, last_name, age, grade):
    cursor.execute("""
        INSERT INTO students (first_name, last_name, age, grade)
        VALUES (%s, %s, %s, %s)
    """, (first_name, last_name, age, grade))

def update_grade(cursor, first_name, new_grade):
    cursor.execute("""
        UPDATE students
        SET grade = %s
        WHERE first_name = %s
    """, (new_grade, first_name))

def delete_student(cursor, last_name):
    cursor.execute("""
        DELETE FROM students
        WHERE last_name = %s
    """, (last_name,))

def fetch_all_records(cursor):
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    for record in records:
        print(record)

def main():
    connection = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password"
    )
    cursor = connection.cursor()

    create_database(cursor)
    create_table(cursor)

    insert_record(cursor, "Alice", "Smith", 18, 95.5)
    update_grade(cursor, "Alice", 97.0)
    delete_student(cursor, "Smith")
    fetch_all_records(cursor)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
