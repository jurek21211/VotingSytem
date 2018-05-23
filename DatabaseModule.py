import MySQLdb


class Database():

    def __init__(self):
        self._dbHost = "sql.s13.vdl.pl"
        self._dbName = "bastionk_votingsystem"
        self._dbUser = "bastionk_vote"
        self._dbPasswd = "Glosowanie12"

    def addYesVote(self):
        db = MySQLdb.connect(host=self._dbHost, user=self._dbUser,
                             passwd=self._dbPasswd, db=self._dbName)

        Cursor = db.cursor()
        # Cursor.execute() Query: Increase YES value by 1
        db.commit()
        db.close()

    def addNoVote(self):
        db = MySQLdb.connect(host=self._dbHost, user=self._dbUser,
                             passwd=self._dbPasswd, db=self._dbName)

        Cursor = db.cursor()
        # Cursor.execute() Query: Increase NO value by 1
        db.commit()
        db.close()

    def isAllowedToVote(self, userID):
        db = MySQLdb.connect(host=self._dbHost, user=self._dbUser,
                             passwd=self._dbPasswd, db=self._dbName)

        Cursor = db.cursor()
        # Cursor.execute() Query: Check if value for specific userID in "voted flag" is Yes or No
        # isAllowed = Cursor.fetchall()
        if isAllowed[0] == "Yes":
            db.close()
            return True

        elif isAllowed[0] == "No":
            db.close()
            return False

    def justVoted(self, userID):
        db = MySQLdb.connect(host=self._dbHost, user=self._dbUser,
                             passwd=self._dbPasswd, db=self._dbName)

        Cursor = db.cursor()
        # Cursor.execute() #Query: Update value on "voted flag" and set to No for specific usedID
        db.commit()
        db.close()
