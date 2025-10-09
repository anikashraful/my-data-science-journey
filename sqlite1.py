import sqlite3

# Connect to database
conn = sqlite3.connect('database.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""
	CREATE TABLE customers(
		id int primary key,
		first_name text,
		last_name text,
		email text
	)
""")

c.execute("INSERT INTO customers VALUES ('01','John','Bar','bar@john.com')")

# show 
c.execute("SELECT * FROM customers")

# print
print(c.fetchall())

# Commit our command
conn.commit()

# Close our connection
conn.close()