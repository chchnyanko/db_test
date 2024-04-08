import sqlite3


is_id = ""


def check_id(results: list, id: str):
    target_id = id.replace("ID", "Name")
    id_table = id.replace("ID", "")
    db = sqlite3.connect("splatoon3.db")
    cursor = db.cursor()
    query = (f"SELECT {target_id} FROM {id_table}")
    cursor.execute(query)
    query_results = cursor.fetchall()
    new_list = []
    for i in results:
        if i[0]:
            new_list.append(query_results[int(i[0]) - 1])
        else:
            new_list.append("")
    print_result(new_list)


def connect(query):
    db = sqlite3.connect("splatoon3.db")
    cursor = db.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        if is_id:
            check_id(results, is_id)
        else:
            print_result(results)
        db.close()
        return results
    except Exception as e:
        print(e, "fail ore")


def print_result(results):
    print(is_id)
    for i in results:
        if i is not None:
            if type(i) is tuple:
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
connect(f"SELECT {target} FROM {table}{filter}")
