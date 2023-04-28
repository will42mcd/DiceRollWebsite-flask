import mysql.connector
import dice_roll_web
mydb = mysql.connector.connect(host= "localhost", user="root", password ="Wbwb1108")

mycursor = mydb.cursor()

mycursor.execute("db_log")

for db in mycursor:
    print(db)