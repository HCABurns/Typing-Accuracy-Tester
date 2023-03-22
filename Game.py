#Imports
import time
import random

class Game():
    """
    This is the game class. This class deals with getting the phrase the user needs to enter.
    This class will also calculate the accuracy of the user.

    Methods
    --------------
    __init__(ui,db) - Defines all the requires variables.
    set_phrase() - Selects and sets a random phrase from the database to use.
    begin() - Starts the game.
    updateDB() - This will update the number of uses and average accuracy of the phrase used.
    calculate_accuracy() - Calculates the accuracy of the user.
    calculate_wpm() - Calculates the words per minute of the user.
    """
    def __init__(self,ui,db):
        """
        This function sets variables that will be required.

        Parameters
        -------------
        ui : UI object
            This is a UI object so that the user input label cab be examined for the user input.
        db : dbController object
            This is a dbControlelr object so the database can be queried and updated.
        """
        self.phrase = ""
        self.answer = ""
        self.start_time = 0
        self.end_time = 0
        self.accuracy = 0.0
        self.id = -1
        self.uses = -1
        self.wpm = 0
        self.ui = ui
        self.db = db
        self.set_phrase()
        

    def set_phrase(self):
        """
        This function will pick a random phrase from the database and store it with the id and uses.
        """
        #Get a value for how many phrases are in the database
        command = "SELECT id FROM Phrases ORDER BY id DESC LIMIT 1"
        rows = self.db.execute(command)
        for row in rows:
            amount = row[0]
        #Pick a random phrase from the database
        command = "SELECT phrase,id,uses from Phrases WHERE id={}".format(random.randint(1,int(amount)))
        rows = self.db.execute(command)
        for row in rows:
            self.phrase = row[0]
            self.id=row[1]
            self.uses=row[2]


    def begin(self):
        """
        This function runs the game loop. It will continueally check the input label and once the input is
        larger than the phrase it will end and calulcate accuracy and wpm.

        Return
        ------------
        list - List of float values indicating the following: [accuracy %, time to complete, wpm, accurate wpm]
        """
        #Get start time
        self.start_time = time.time()
        chars = 0
        print(self.phrase)
        #Loop through and check how many chars the user has entered
        while True:
            try:
                if len(self.ui.inputLabel.cget("text")) >= len(self.phrase): #while chars < len(self.phrase)
                    break
            except:
                return 0
        #Calculate the accuracy and wpm
        self.answer = self.ui.inputLabel.cget("text")
        self.end_time = time.time()
        self.calculate_accuracy()
        self.calculate_wpm()
        print("Accuracy: {}% in {}s".format(self.accuracy,self.end_time-self.start_time))
        print("WPM: {}".format(self.wpm))
        print("Accurate WPM: {}".format(self.wpm /100 * self.accuracy))
        #Update database and return
        self.updateDB()
        return [self.accuracy,self.end_time-self.start_time, self.wpm, self.wpm /100 * self.accuracy]


    def updateDB(self):
        """
        This function will update the uses and average accuracy of the used phrase in game.
        """
        #Find the correct phrase
        command = "SELECT avgAccuracy FROM Phrases WHERE phrase='{}'".format(self.phrase)
        result = self.db.execute(command)
        for each in result:
            score = each[0]
        #Update the uses and accuracy
        command = "UPDATE Phrases SET uses={},avgAccuracy={} WHERE phrase='{}';".format(self.uses+1,(score + self.accuracy)/2,self.phrase)
        self.db.execute(command)
        self.db.commit()

        
    def calculate_accuracy(self):
        """
        This function will calculate the accuracy and update the accuracy variable.
        """
        equal = 0
        for char1,char2 in zip(self.answer,self.phrase):
            if char1 == char2:
                equal+=1
        self.accuracy = equal / len(self.phrase) * 100


    def calculate_wpm(self):
        """
        This function will calculate the words per minute and update the wpm variable.
        """
        total_time = self.end_time - self.start_time
        total_words = len(self.phrase.split(" "))
        self.wpm = total_words / total_time * 60
