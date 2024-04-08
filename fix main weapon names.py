import sqlite3


db = sqlite3.connect("splatoon3.db")
cursor = db.cursor()
cursor.execute("SELECT MainWeaponName FROM MainWeapon;")
results = cursor.fetchall()
for i in range(len(results)):
    print(results[i][0])
    if results[i][0].find(" ") == 0:
        query = "UPDATE MainWeapon SET MainWeaponName = ? WHERE MainWeaponID = ?;"
        cursor.execute(query, [str(results[i][0].replace(" ", "")), int(i + 1)])
db.commit()

db.close()
