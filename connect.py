import sqlite3

db = sqlite3.connect("splatoon3.db")
cursor = db.cursor()
sql = "SELECT * FROM MainWeapon;"
cursor.execute(sql)
results = cursor.fetchall()

for name in results:
    if name[1] is not None:
        print(name[1])

db.close()
