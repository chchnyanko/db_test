from bs4 import BeautifulSoup
import csv

import sqlite3

htmlFILE = open("weapondata.html", "r", encoding="utf-8")

html = htmlFILE.read()

soup = BeautifulSoup(html, "html.parser")

data = soup.find_all("table", {'class': 'wikitable sitecolor-s2 sortable mw-collapsible mw-collapsed'})
data_table = []
data_table = data[0].text.split("\n")
str_list = list(filter(None, data_table))

del str_list[:7]
data_table = []
counter = 0
for i in str_list:
    match counter:
        case 0:
            name = i
            counter += 1
        case 1:
            Range = i
            counter += 1
        case 2:
            Damage = i
            counter += 1
        case 3:
            Fire_rate = i
            counter += 1
        case 4:
            Ink_usage = i
            counter += 1
        case 5:
            Mobility = i
            counter += 1
        case 6:
            Paint_rate = i
            data_table.append([name, Range, Damage, Fire_rate, Ink_usage, Mobility, Paint_rate])
            counter = 0
print(data_table)
db = sqlite3.connect("splatoon3.db")
cursor = db.cursor()
for weapons in data_table:
    cursor.execute("INSERT INTO MainWeapon (MainWeaponName, Range, Damage, InkUsage, AttackRate, SpeedWhileShooting) VALUES (?, ?, ?, ?, ?, ?);", (weapons[0], float(weapons[1]), float(weapons[2]), float(weapons[5]), float(weapons[3]), float(weapons[6])))
db.commit()

db.close()
