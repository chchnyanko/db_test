import sqlite3


is_id = ""

db = sqlite3.connect("splatoon3.db")
cursor = db.cursor()

mains = []
subs = []
specials = []


def get_all(table):
    query = f"SELECT {table}Name FROM {table}"
    cursor.execute(query)
    results = cursor.fetchall()
    if table == "MainWeapon":
        for i in results:
            mains.append(i[0])
    if table == "SubWeapon":
        for i in results:
            subs.append(i[0])
    if table == "SpecialWeapon":
        for i in results:
            specials.append(i[0])


def print_all():
    print_columns("Weapons")
    cursor.execute("SELECT * FROM Weapons")
    results = cursor.fetchall()
    for i in range(len(results)):
        if results[i][2]:
            print(results[i][1], ", ", mains[int(results[i][2]) - 1], ", ", subs[int(results[i][3]) - 1], ", ", specials[int(results[i][4]) - 1])


def print_columns(table):
    query = f"SELECT * FROM {table}"
    cursor.execute(query)
    column_names = [description[0] for description in cursor.description]
    print("Column names:", column_names)


def print_stat(table, weapon):
    query = f"SELECT * FROM {table} WHERE {table}Name IS '{weapon}';"
    cursor.execute(query)
    column_names = [description[0] for description in cursor.description]
    print(column_names)
    results = cursor.fetchall()
    print(results)


def _ready():
    get_all("MainWeapon")
    get_all("SubWeapon")
    get_all("SpecialWeapon")
    print("Welcome to the Splatoon 3 database")
    while True:
        print("Enter 'print' to see all of the weapons and their sub and special weapons, ")
        print("Or enter a weapon to see it's stats")
        user_input = input("")
        if user_input.lower() == "print":
            print_all()
        elif user_input in mains:
            print("Weapon")
            print_stat("MainWeapon", user_input)
        elif user_input in subs:
            print("Sub")
            print_stat("SubWeapon", user_input)
        elif user_input in specials:
            print("Special")
            print_stat("SpecialWeapon", user_input)
        elif user_input.lower() == "quit":
            print("Closing...")
            break
        else:
            print("Incorrect Input")


_ready()
