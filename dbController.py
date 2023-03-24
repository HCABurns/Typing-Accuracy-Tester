#Imports
import sqlite3

class DBController():
    """
    This class deals with requests to the database.

    Methods
    -----------
    __init__ - Creates a connection the the database
    execute(command) - Executes a given command (String) on the database.
    commit - Commits any changes to the database.
    """

    def __init__(self):
        #Database connection
        self.con = sqlite3.connect('typingTester.db', check_same_thread=False)
        self.cur = self.con.cursor()


    def execute(self,command):
        return self.cur.execute(command)
        

    def commit(self):
        self.con.commit()


    def getScores(self,phraseID=None):
        """
        This function will return the scores in the database. It will return only those with the phraseID provided
        or will return all if the phraseID is not provided.

        Parameters
        ---------------
        phraseID : int
            This is the phraseID that will be used to find all scores for that phrase.

        Return
        ---------------
        list - List of tuples in the form (name,score)
        """
        if phraseID:
            command = f'SELECT name,score FROM Scores WHERE phraseID="{phraseID}"'
        else:
            command = 'SELECT name,score FROM Scores'

        scores = []
        rows = self.execute(command)
        for row in rows:
            scores.append((row[0],row[1]))        
        return scores
    

    def close(self):
        self.commit()
        self.con.close()
