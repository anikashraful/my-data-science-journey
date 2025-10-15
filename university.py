import sqlite3

conn = sqlite3.connect('university.db')
c = conn.cursor()

# Drop tables if exist
c.execute('DROP TABLE IF EXISTS enrollments')
c.execute('DROP TABLE IF EXISTS students')
c.execute('DROP TABLE IF EXISTS courses')
c.execute('DROP TABLE IF EXISTS instructors')

# Create instructors table
c.execute('''
CREATE TABLE instructors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL
)
''')

# Create courses table
c.execute('''
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    credits INTEGER NOT NULL CHECK (credits > 0),
    instructor_id INTEGER NOT NULL,
    FOREIGN KEY (instructor_id) REFERENCES instructors (id) ON DELETE CASCADE
)
''')

# Create students table
c.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    major TEXT NOT NULL,
    enrollment_year INTEGER NOT NULL CHECK (enrollment_year >= 2020)
)
''')

# Create enrollments table
c.execute('''
CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    grade REAL CHECK (grade >= 0 AND grade <= 100),
    FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses (id) ON DELETE CASCADE,
    UNIQUE (student_id, course_id)
)
''')

# Insert instructors
c.executemany("INSERT INTO instructors (name, department) VALUES (?, ?)", [
    ('Dr. Alice Smith', 'Computer Science'),
    ('Prof. Bob Johnson', 'Mathematics'),
    ('Dr. Carol Davis', 'Physics')
])

# Insert courses
c.executemany("INSERT INTO courses (name, credits, instructor_id) VALUES (?, ?, ?)", [
    ('Intro to Programming', 3, 1),
    ('Data Structures', 4, 1),
    ('Calculus I', 4, 2),
    ('Linear Algebra', 3, 2),
    ('Quantum Mechanics', 4, 3),
    ('Electromagnetism', 3, 3)
])

# Insert students
c.executemany("INSERT INTO students (name, major, enrollment_year) VALUES (?, ?, ?)", [
    ('Emma Wilson', 'Computer Science', 2023),
    ('Liam Brown', 'Mathematics', 2022),
    ('Olivia Taylor', 'Physics', 2024),
    ('Noah Garcia', 'Computer Science', 2023),
    ('Sophia Martinez', 'Mathematics', 2023)
])

# Insert enrollments
c.executemany("INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)", [
    (1, 1, 95),  
    (1, 2, 88),  
    (1, 3, 92), 
    (2, 3, 87), 
    (2, 4, 94),  
    (3, 5, 76),  
    (3, 6, 89),  
    (4, 1, 91),  
    (4, 2, 96),  
    (5, 4, 85)   
])

conn.commit()
conn.close()