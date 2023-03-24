#Imports
import sqlite3
import socket
import re

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
            command = f'SELECT name,score FROM Scores WHERE phraseID="{phraseID}";'
        else:
            command = 'SELECT name,score FROM Scores;'

        #Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 55555
        client_socket.connect((host, port))
        #Send query
        client_socket.sendall(command.encode('utf-8'))


        #Get the response and return it 
        scores = client_socket.recv(1024).decode('utf-8')
        
        x = re.split('[()]', scores)
        scores = []
        for pair in x:
            if len(pair) > 2:
                split = pair.split(",")
                print(split)
                scores.append(("".join([i for i in split[0][1:len(split[0])-1] if i.isalpha()]), int("".join([i for i in split[1] if i.isnumeric()]))))
                print(("".join([i for i in split[0][1:len(split[0])-1] if i.isalpha()]), int("".join([i for i in split[1] if i.isnumeric()]))))
        #Close the client socket
        client_socket.close()       
        return scores
    

    def close(self):
        self.commit()
        self.con.close()
