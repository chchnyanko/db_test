import sqlite3


is_id = ""

mains = []
subs = []
specials = []


def get_all_mains():
    db = sqlite3.connect("splatoon3.db")
    cursor = db.cursor()
    cursor.execute("SELECT MainWeaponName FROM MainWeapon")
    results = cursor.fetchall()
    for i in results:
        mains.append(i[0])
    db.close()


def get_all_subs():
    db = sqlite3.connect("splatoon3.db")
    cursor = db.cursor()
    cursor.execute("SELECT SubWeaponName FROM SubWeapon")
    results = cursor.fetchall()
    for i in results:
        subs.append(i[0])
    db.close()


def get_all_specials():
    db = sqlite3.connect("splatoon3.db")
    cursor = db.cursor()
    cursor.execute("SELECT SpecialWeaponName FROM SpecialWeapon")
    results = cursor.fetchall()
    for i in results:
        specials.append(i[0])
    db.close()


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
        print(e, "failure")
        query()


def print_result(results):
    print(is_id)
    for i in results:
        if i is not None:
            if type(i) is tuple:
                i = i[0]
            print(i)


def print_weapons_as_list():
    db = sqlite3.connect("splatoon3.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Weapons")
    results = cursor.fetchall()
    for i in range(len(results)):
        if results[i][2]:
            print(results[i][0], ", ", results[i][1], ", ", mains[int(results[i][2]) - 1], ", ", subs[int(results[i][3]) - 1], ", ", specials[int(results[i][4]) - 1])


def intro():
    db = sqlite3.connect("splatoon3.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Weapons")
    column_names = [description[0] for description in cursor.description]
    print("Column names:", column_names)
    db.close()


def query():
    target = input("What are you looking for ")
    table = input("Where is it from ")
    limit = input("Do you want any filters leave blank if not ")
    filter = ""
    if target.lower().find("id") != -1:
        is_id = target
    if limit:
        filter = (f" WHERE {limit}")
    connect(f"SELECT {target} FROM {table}{filter}")


def _ready():
    get_all_mains()
    get_all_subs()
    get_all_specials()
    intro()
    print_weapons_as_list()
    # query()


_ready()
