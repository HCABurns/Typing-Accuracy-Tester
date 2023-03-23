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


    def close(self):
        self.commit()
        self.con.close()
