import time
import random
from dbController import dbController

class Game():
    """
    This is the game class.
    """
    def __init__(self):
        self.phrase = ""
        self.answer = ""
        self.start_time = 0
        self.end_time = 0
        self.accuracy = 0.0
        self.id = -1
        self.uses = -1
        self.wpm = 0
        self.db = dbController()
        self.set_phrase()
        

    def set_phrase(self):
        command = "SELECT id FROM Phrases ORDER BY id DESC LIMIT 1"
        rows = self.db.execute(command)
        for row in rows:
            amount = row[0]
        command = "SELECT phrase,id,uses from Phrases WHERE id={}".format(random.randint(1,int(amount)))
        rows= self.db.execute(command)
        for row in rows:
            self.phrase = row[0]
            self.id=row[1]
            self.uses=row[2]
            print(self.uses)

    def begin(self):
        #Get start time
        self.start_time = time.time()
        chars = 0
        print(self.phrase)
        #Loop through and check how many chars the user has entered (Need tkinter first)
        while len(ui.inputLabel.cget("text")) < len(self.phrase): #while chars < len(self.phrase) 
            continue
            #break
        self.answer = ui.inputLabel.cget("text")
        self.end_time = time.time()
        self.calculate_accuracy()
        self.calculate_wpm()
        print("Accuracy: {}% in {}s".format(self.accuracy,self.end_time-self.start_time))
        print("WPM: {}".format(self.wpm))
        print("Accurate WPM: {}".format(self.wpm /100 * self.accuracy))
        self.updateDB()

    def updateDB(self):
        command = "SELECT avgAccuracy FROM Phrases WHERE phrase='{}'".format(self.phrase)
        result = self.db.execute(command)
        for each in result:
            score = each[0]
        
        command = "UPDATE Phrases SET uses={},avgAccuracy={} WHERE phrase='{}';".format(self.uses+1,(score + self.accuracy)/2,self.phrase)
        print(command)
        self.db.execute(command)
        self.db.commit()

        
    def calculate_accuracy(self):
        equal = 0
        for i in range(len(self.answer)):
            if self.answer[i] == self.phrase[i]:
                equal += 1
        self.accuracy = equal / len(self.phrase) * 100

    def calculate_wpm(self):

        total_time = self.end_time - self.start_time
        total_words = len(self.phrase.split(" "))
        self.wpm = total_words / total_time * 60
