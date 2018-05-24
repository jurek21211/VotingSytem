from DatabaseModule import Database
class Administrator():

    def __init__(self):
        self._adminID = None #Administrator Card ID
        self._db = Database()


    def startPoll(self):
        db = self._db.dbConnect()

        Cursor = db.cursor()
        Cursor.execute('Query') 
        db.commit()
        db.close()