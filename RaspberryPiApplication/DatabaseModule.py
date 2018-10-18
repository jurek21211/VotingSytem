import MySQLdb


class Database():

    def __init__(self):
        self._dbHost = "sql.s13.vdl.pl"
        self._dbName = "bastionk_votingsystem"
        self._dbUser = "bastionk_vote"
        self._dbPasswd = "Glosowanie12"



    def dbConnect(self):
        return MySQLdb.connect(host=self._dbHost, user=self._dbUser,
                             passwd=self._dbPasswd, db=self._dbName)

    def ifopen(self):
        db = self.dbConnect()
        Cursor = db.cursor()
        Cursor.execute("SELECT closed FROM Polls WHERE closed = 'open'")
        Result = Cursor.fetchall()
        if Result == ():
            return False
        else:
            return True
    def TEST(self, userID):
        
        db = self.dbConnect()

        Cursor = db.cursor()
        Cursor.execute("SELECT Voted FROM voters WHERE Card_ID = %s", [userID])
       # Cursor.execute("SELECT NOW()")
        result = Cursor.fetchall()

        #for row in result:
         #   print(row)
	return (result)
        db.close()

    def addYesVote(self):
        db = self.dbConnect()

        Cursor = db.cursor()
        Cursor.execute("UPDATE Polls SET yes_votes = yes_votes + 1 WHERE closed = 'open'") #Query: Increase YES value by 1
        db.commit()
        db.close()

    def addNoVote(self):

        db = self.dbConnect()

        Cursor = db.cursor()
        Cursor.execute("UPDATE Polls SET no_votes = no_votes + 1 WHERE closed = 'open'") #Query: Increase NO value by 1
        db.commit()
        db.close()

    def isAllowedToVote(self,userID):
        db = self.dbConnect()
        Voted_Cursor = db.cursor()

        Voted_Cursor.execute("SELECT Voted FROM voters WHERE Card_ID = %s", [userID] ) #Query: Check if value for specific userID in "voted flag" is Yes or No
        
        Voted = Voted_Cursor.fetchall()
        if Voted != ():
            if Voted[0][0] == 'yes' :
                db.close()
                return 0

            elif Voted[0][0] == 'no':
                db.close()
                return 1
        else:
            return -1
    def setVotedToYes(self, userID):
        db = self.dbConnect()

        Cursor = db.cursor()
        Cursor.execute("UPDATE voters SET Voted = 'yes' WHERE Card_ID = %s", [userID] ) #Query: Update value on "voted flag" and set to No for specific usedID
        db.commit()
        db.close()

