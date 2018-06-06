from DatabaseModule import Database
from datetime import datetime
import LCD

class Administrator():

    def __init__(self):
        self._adminID = None #Administrator Card ID
        self._db = Database()


    def startPoll(self):
        db = self._db.dbConnect()
        Cursor = db.cursor()
        Cursor.execute("INSERT INTO Polls (poll_name, closed, yes_votes, no_votes) VALUES (NOW(), 'open', 0, 0)")
        db.commit()
        db.close()

    def setVotedToNo(self):
        db = self._db.dbConnect()

        Cursor = db.cursor()
        Cursor.execute("UPDATE voters SET Voted = 'no'")
        db.commit()
        db.close()

    def closeVoting(self):
        db = self._db.dbConnect()

        Cursor = db.cursor()
        Cursor.execute("UPDATE Polls SET closed = 'closed' WHERE closed = 'open'")
        db.commit()
        db.close()
    def Archive(self):
        mylcd = LCD.lcd()
        db=self._db.dbConnect()
        Cursor = db.cursor()
        Cursor.execute("SELECT DATE_FORMAT(poll_name,'%Y %m %d %H %i %s'),yes_votes,no_votes FROM Polls WHERE closed = 'closed'")
        result = Cursor.fetchall()
        currDay= datetime.now()
        with open("Archive", "w") as archive:
            archive.write("Copy created: {}\n".format(currDay))
            archive.write("Date\t\t\t YES\tNO\n")
            for row in result:
                archive.write(str(row)+"\n") 
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Backup DONE",1)
        db.close()