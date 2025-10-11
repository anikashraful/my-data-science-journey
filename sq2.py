import sqlite3

# Connect to a database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()


# Create a table
cursor.execute("""
	CREATE TABLE IF NOT EXISTS employees(
		id int primary key,
		name text,
		dept text,
		salary real

	)
""")

# Insert values
cursor.execute("INSERT INTO employees (id, name, dept, salary) values (?, ?, ?, ?)", (1, 'Anik', 'Research', 100000))

# Update values
cursor.execute('UPDATE employees SET salary = ? WHERE name = ?', (100000, 'Anik'))

# Delete employees
cursor.execute('DELETE FROM employees WHERE name = ?', ('BOB'))


# select all column from employees
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
for row in rows:
	print(row)


# Commit & close
conn.commit()
conn.close()