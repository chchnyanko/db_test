import sqlite3


def connect(query):
    db = sqlite3.connect("splatton3.db")
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print_result(results)
    return results
    db.close()


def print_result(results):
    for i in results:
        if results.type == list:
            if i[1] is not None:
                print(i[1])


connect("SELECT * FROM Weapons")
