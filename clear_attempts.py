import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("DELETE FROM login_attempts")
conn.commit()
conn.close()
print("Login attempts cleared.")
