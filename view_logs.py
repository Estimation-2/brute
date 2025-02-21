import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("SELECT * FROM login_attempts")
attempts = c.fetchall()

print("Login Attempts:")
for attempt in attempts:
    print(attempt)

conn.close()
