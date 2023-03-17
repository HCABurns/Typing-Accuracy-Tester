import sqlite3

class dbController():

    def __init__(self):
        #Database connection
        self.con = sqlite3.connect('phrases.db', check_same_thread=False)
        self.cur = self.con.cursor()


    def execute(self,command):
        return self.cur.execute(command)
        

    def commit(self):
        self.cur.commit()
