"""
Correct the below code so that the output should be the version
number.
"""

import sqlite3
con = sqlite3.connect('test.db')
with con:
 cur = con.cursor()
 cur.execute('SELECT SQLITE_VERSION()')   #Modified the query so as to include for SQL_LITE_VERSION
 data = cur.fetchone()
 print ("SQLite version: %s" % data)


"""
Correct the below program so that it should display the last
inserted row id.
"""
con = sqlite3.connect('new_db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE Friends")
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
    number_of_rows = cur.execute("SELECT Count(Id) from Friends").lastrowid
    print("The last Id of the inserted row is %d",number_of_rows)

"""
Correct the below code so that it checks weather database exists
or not.
"""
import os  #This import can be removed.
import sqlite3
db_filename = 'todo.db'
db_is_new = not os.path.isfile(db_filename)
conn = sqlite3.connect(db_filename)
if db_is_new:
 print ('Need to create schema')
 print ('Creating database')
else:
 print ('Database exists, assume schema does, too.')
conn.close()


"""
If Car is a table already created. What is the key word in place of
“XXXX” to be used to display the column names of Cars table?
"""
import sqlite3 as lite
import sys   #Import can also be removed.
con = lite.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    for colinfo in cur.fetchall():  #Fetchall is the command
        print (colinfo)



"""
Below program is for creating car’s table and inserting values.
But some corrections are needed. Correct the errors and execute
this code.
"""
import sqlite3 as lite
#Modified the tuple car to list of tuples
cars = [
 (1, 'Audi', 52642),
 (2, 'Mercedes', 57127),
 (3, 'Skoda', 9000),
 (4, 'Volvo', 29000),
 (5, 'Bentley', 350000),
 (6, 'Hummer', 41400),
 (7, 'Volkswagen', 21600)
]

con = lite.connect('test.db')
with con:
 cur = con.cursor()
 cur.execute("DROP TABLE IF EXISTS Cars")
 cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
 cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
 #print("Number of cars inserted: ", cur.execute("Select count(*) from Cars").lastrowid)  Added this line for checking


"""
If the question 5 is successfully executed then retrieve the data
by correcting the below code.
"""
import sqlite3 as lite
con = lite.connect('test.db')
with con:
 cur = con.cursor()
 cur.execute("SELECT * FROM Cars")
 rows = cur.fetchall()    #fetchAll is the API that needs to be used
 for row in rows:
    print (row)


"""
Correct the below code. [Note: Question 5 should be successfully
executed]
"""
import sqlite3 as lite
con = lite.connect('test.db')
with con:

 con.row_factory = lite.Row
 cur = con.cursor()
 cur.execute("SELECT * FROM Cars")
 rows = cur.fetchall()
 for row in rows:
     print ("%s %s %s" % (row["Id"], row["Name"], row["Price"]))


"""
Correct the below code and it should update the values
"""
import sqlite3 as lite
import sys
uId = 1
uPrice = 62300
con = lite.connect('test.db')
with con:
 cur = con.cursor()
 cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))
 con.commit()

 print ("Number of rows updated: %d" % cur.rowcount)

"""
Correct the below code so that it displays the metadata info of
the cars table.
"""

import sqlite3 as lite
con = lite.connect('test.db')
with con:

 cur = con.cursor()

 cur.execute("PRAGMA  table_info('Cars')")

 data = cur.fetchall()

 for d in data:
    print (d[0], d[1], d[2])


"""
Correct the below code so that it displays all the rows from the
Cars table with their column names.

"""
import sqlite3 as lite
con = lite.connect('test.db')
with con:

 cur = con.cursor()
 cur.execute('SELECT * FROM Cars')

 col_names = [cn[0] for cn in cur.description]

 rows = cur.fetchall()

 print ("%s %-10s %s" % (col_names[0], col_names[1], col_names[2]))
 for row in rows:
    print ("%2s %-10s %s" % row)

"""
Write python program which loads “sample-storedata.csv” file
data into “store” table in sqlite3.
“sample-storedata.csv” is supplied.

"""
import csv, sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE Store (col1, col2);") # use your column names here

with open('data.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['col1'], i['col2']) for i in dr]

cur.executemany("INSERT INTO Store (col1, col2) VALUES (?, ?);", to_db)
con.commit()
con.close()

"""
Fetch all the rows in store table created
"""
import sqlite3 as lite
con = lite.connect(':memory:')
with con:
 cur = con.cursor()
 cur.execute("SELECT * FROM Store")
 rows = cur.fetchall()

"""
Fetch the column names of the store table created.
"""
import sqlite3 as lite
con = lite.connect(':memory:')
with con:
 cur = con.cursor()
 cur.execute('SELECT * FROM Store')
 col_names = [cn[0] for cn in cur.description]

