import sqlite3

conn = sqlite3.connect('employeee.db')
c = conn.cursor()

# Drop if exists
c.execute('DROP TABLE IF EXISTS departments')
c.execute('DROP TABLE IF EXISTS employeees')

# Department table
c.execute('''
	CREATE TABLE departments(
		dept_id int primary key,
		dept_name text not null unique,
		location text
	)
''')
depts_data = [(1, 'HR','New York'),(2, 'ENG','San Fransisco'), (3, 'Sales', 'Chicago'), (4, 'Marketing', 'Los Angeles')]
c.executemany('INSERT INTO departments(dept_id, dept_name, location) VALUES (?, ?, ?)', depts_data)

# Employees table
c.execute('''
	CREATE TABLE employeees(
		id int primary key,
		name text not null,
		dept_id int,
		salary real,
		hire_date DATE,
		FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
	)
''')

emp_data = [
    (1, 'Alice', 1, 60000, '2023-01-15'), (2, 'Bob', 2, 80000, '2022-05-10'),
    (3, 'Charlie', 1, 55000, '2024-03-20'), (4, 'Diana', 2, 75000, '2022-11-05'),
    (5, 'Eve', 3, 70000, '2023-08-12'), (6, 'Frank', 3, 65000, '2024-02-28'),
    (7, 'Grace', 2, 90000, '2021-09-01'), (8, 'Henry', 1, 62000, '2023-12-10'),
    (9, 'Ivy', 3, 68000, '2025-01-01'), (10, 'Jack', 4, 72000, '2024-06-15')
]
c.executemany("INSERT INTO employeees (id, name, dept_id, salary, hire_date) VALUES (?, ?, ?, ?, ?)", emp_data)
conn.commit()

# Inner join
c.execute('''
	SELECT e.name, e.salary, d.dept_name, d.location
	FROM employeees e 
	INNER JOIN departments d ON e.dept_id = d.dept_id
	ORDER BY e.name
''')
#for row in c.fetchall():
	#print(row)

# Employees with their department's average salary
c.execute('''
	SELECT e.name, e.salary,
		(SELECT AVG(salary) FROM employeees e2 WHERE e2.dept_id = e.dept_id) as dept_avg
	FROM employeees e
	ORDER BY e.name
''')
for row in c.fetchall():
	print(row)

conn.close()