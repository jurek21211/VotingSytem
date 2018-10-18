"""import MySQLdb

db = MySQLdb.connect(host="sql.s13.vdl.pl", user="bastionk_vote",
                             passwd="Glosowanie12", db="bastionk_votingsystem")

Cursor = db.cursor()
Cursor.execute("SELECT * FROM Test")
result = Cursor.fetchall()

for row in result:
    print (row)


db.close()"""

from DatabaseModule import Database

Database = Database()

print (Database.TEST(3))