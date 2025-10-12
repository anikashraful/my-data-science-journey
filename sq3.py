# Import SQLite3 in Python
import sqlite3

# Creating Database
conn = sqlite3.connect('employee.db')
c = conn.cursor()

# Drop if exists for clean start
c.execute('DROP TABLE IF EXISTS employee')


# Creating table
c.execute('''
	CREATE TABLE employee(
		id int primary key,
		name text not null,
		dept text,
		salary real,
		hire_date DATE
	)
''')

# Inserting Data
initial_data = [
	( 1, 'Alice',   'HR',    60000,  '2023-01-15'),
	( 2, 'Bob',     'ENG',   80000,  '2022-01-10'),
	( 3, 'Charlie', 'HR',    55000,  '2024-01-15'),
	( 4, 'Diana',   'ENG',   75000,  '2021-01-15'),
	( 5, 'Eve',     'SALES', 70000,  '2023-01-15'),
	( 6, 'Frank',   'SALES', 65000,  '2024-11-15'),
	( 7, 'Grace',   'ENG',   95000,  '2021-11-05'),
	( 8, 'Henry',   'HR',    65000,  '2023-11-05')
]

c.executemany("INSERT INTO employee (id, name, dept, salary, hire_date) values (?, ?, ?, ?, ?)", initial_data)
conn.commit()

# Verify
c.execute('SELECT * FROM employee ORDER BY id')
for row in c.fetchall():
	print(row)

conn.close()