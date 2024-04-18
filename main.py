'''Program to view data from the splatoon3.db database'''


# importing sqlite3 to access the database
import sqlite3


import string


# variables used to access the database
db = sqlite3.connect("splatoon3.db")
cursor = db.cursor()


# lists holding the names of the weapons
mains = []
subs = []
specials = []
maintypes = []


# function called at the beggining of the program used to add all of the weapons to the lists above
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


# same as the function above but used for weapon types instead of names
def get_weapon_types():
    query = "SELECT WeaponType FROM WeaponTypes"
    cursor.execute(query)
    results = cursor.fetchall()
    for i in results:
        maintypes.append(i[0])


# prints all of the names of the weapon, main weapon, sub weapon and the special weapon of each of the weapons
def print_all():
    print("")
    print("Weapon Name                   Main Weapon Name              Sub Weapon Name     Special Weapon Name")
    print("---------------------------------------------------------------------------------------------------")
    cursor.execute("SELECT * FROM Weapons")
    results = cursor.fetchall()
    for i in range(len(results)):
        if results[i][2]:
            print(f"{results[i][1]:<30}{mains[int(results[i][2]) - 1]:<30}{subs[int(results[i][3]) - 1]:<20}{specials[int(results[i][4]) - 1]:<20}")


#prints the help screen
def print_help():
    print("Input                          Result")
    print("------------------------------------------------------------------------------------------------")
    print("Print                          Shows all of the weapons and their Main, Sub and Specials weapons")
    print("Mains                          Shows all if the stats of all of the Main Weapons")
    print("Subs                           Shows all if the stats of all of the Sub Weapons")
    print("Specials                       Shows all if the stats of all of the Special Weapons")
    print("Name of any Main Weapon        Shows all of the stats of that Main Weapon")
    print("Name of any Sub Weapon         Shows all of the stats of that Sub Weapon")
    print("Name of any Special Weapon     Shows all of the stats of that Special Weapon")


# prints all of the stats for the main weapons
def print_mains(weapon):
    print("")
    print("MainWeaponName                WeaponType     Damage         Range          AttackRate     InkUsage       SpeedWhileShooting")
    print("---------------------------------------------------------------------------------------------------------------------------")
    query : str
    if weapon == "all":
        query = "SELECT * FROM MainWeapon;"
    else:
        query = f"SELECT * FROM MainWeapon WHERE MainWeaponName IS '{weapon}';"
    cursor.execute(query)
    results = cursor.fetchall()
    results_list : list = []
    for i in results:
        results_list.clear()
        for x in i:
            if x == 0:
                results_list.append("N/A")
            else:
                results_list.append(x)
        print(f"{results_list[1]:<30}{maintypes[results_list[2] - 1]:<15}{results_list[3]:<15}{results_list[4]:<15}{results_list[5]:<15}{results_list[6]:<15}{results_list[7]:<15}")


# prints all of the stats for the sub weapons
def print_subs(weapon):
    print("")
    print("SubWeaponName                 Damage         Ink            Tracking       DamageDuration")
    print("-----------------------------------------------------------------------------------------")
    query : str
    if weapon == "all":
        query = "SELECT * FROM SubWeapon;"
    else:
        query = f"SELECT * FROM SubWeapon WHERE SubWeaponName IS '{weapon}';"
    cursor.execute(query)
    results = cursor.fetchall()
    for i in results:
        print(f"{i[1]:<30}{i[2]:<15}{i[3]:<15}{i[4]:<15}{i[5]:<15}")


# prints all of the stats for the special weapons
def print_specials(weapon):
    print("")
    print("SpecialWeaponName             Damage              NumberOfAttacks     Duration")
    print("------------------------------------------------------------------------------")
    query : str
    if weapon == "all":
        query = "SELECT * FROM SpecialWeapon;"
    else:
        query = f"SELECT * FROM SpecialWeapon WHERE SpecialWeaponName IS '{weapon}';"
    cursor.execute(query)
    results = cursor.fetchall()
    for i in results:
        print(f"{i[1]:<30}{i[2]:<20}{i[3]:<20}{i[4]:<20}")


# function called at the beggining of the program
def _ready():
    get_all("MainWeapon")
    get_all("SubWeapon")
    get_all("SpecialWeapon")
    get_weapon_types()
    print("")
    print("Welcome to the Splatoon 3 database")
    while True:
        print("")
        print("Enter an input")
        print("Or enter 'Help' to see what you can do")
        print("")
        user_input = input("")
        if user_input.lower() == "print":
            print_all()
        elif user_input.lower() == "help":
            print_help()
        elif string.capwords(user_input) in mains:
            print_mains(string.capwords(user_input))
        elif user_input.upper() in mains:
            print_mains(user_input.upper())
        elif string.capwords(user_input) in subs:
            print_subs(string.capwords(user_input))
        elif string.capwords(user_input) in specials:
            print_specials(string.capwords(user_input))
        elif user_input.lower() == "mains":
            print_mains("all")
        elif user_input.lower() == "subs":
            print_subs("all")
        elif user_input.lower() == "specials":
            print_specials("all")
        elif user_input.lower() == "quit":
            print("Closing...")
            db.close()
            break
        else:
            print("Incorrect Input")


_ready()
