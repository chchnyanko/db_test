import sqlite3


is_id = ""


def check_id(id: str):
    print(id)
    target_id = id.replace("ID", "Name")
    id_table = id.replace("ID", "")
    print(f"SELECT {target_id} FROM {id_table};")
    connect(f"SELECT {target_id} FROM {id_table};")


def connect(query):
    db = sqlite3.connect("splatoon3.db")
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print_result(results)
    db.close()
    return results


def print_result(results):
    print(is_id)
    for i in results:
        if i is not None:
            if type(i) == tuple:
                i = i[0]
            print(i)


target = input("What are you looking for ")
table = input("Where is it from ")
limit = input("Do you want any filters leave blank if not ")
filter = ""
if target.lower().find("id") != -1:
    is_id = target
if limit:
    filter = (f" WHERE {limit}")
if is_id:
    check_id(is_id)
else:
    connect(f"SELECT {target} FROM {table}{filter}")

