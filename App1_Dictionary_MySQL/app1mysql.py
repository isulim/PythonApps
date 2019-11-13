import mysql.connector

conn = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = conn.cursor()

word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(word))
results = cursor.fetchall()

if results:
    for index, result in enumerate(results):
        print(str(index + 1) + ") " + result[1])
else:
    print("No such word found in dictionary.")