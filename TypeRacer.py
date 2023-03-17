#Imports
from tkinter import *
import time
import random
import sqlite3
import threading

#Database connection
con = sqlite3.connect('phrases.db', check_same_thread=False)
cur = con.cursor()

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
        self.set_phrase()

    def set_phrase(self):
        command = "SELECT id FROM Phrases ORDER BY id DESC LIMIT 1"
        rows = cur.execute(command)
        for row in rows:
            amount = row[0]
        command = "SELECT phrase,id,uses from Phrases WHERE id={}".format(random.randint(1,int(amount)))
        rows = cur.execute(command)
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
        result = cur.execute(command)
        for each in result:
            score = each[0]
        
        command = "UPDATE Phrases SET uses={},avgAccuracy={} WHERE phrase='{}';".format(self.uses+1,(score + self.accuracy)/2,self.phrase)
        print(command)
        cur.execute(command)
        con.commit()

        
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

def playGame(label):
    main = Game()
    ui.set_phraseUI(main.phrase)
    ui.start_countdown(label)
    ui.setBind()
    main.begin()
    ui.unbind()
    

class UI():
    """
    This is the class to deal with the UI.
    """
    def __init__(self):
        self.root = Tk()
        #self.root.bind('<Key>', ui.key_press)
        self.root.geometry("{}x{}".format(800, 480))
        self.root.title("Typing Speed Calculator")
        self.root.iconphoto(False, PhotoImage(file='logo.png'))
        self.set_UI()

    def setBind(self):
        self.root.bind('<Key>', ui.key_press)
        print("yeah")

    def unbind(self):
        self.root.unbind('<Key>')

    def key_press(self,event):
        if event.keysym == "BackSpace":
            self.inputLabel.config(text="{}".format(self.inputLabel.cget("text")[0:-1]))
        else:
            self.inputLabel.config(text="{}".format(self.inputLabel.cget("text") + event.char))

    def alter_label(label,newText):
        label.config(text = newText)

    def start_countdown(self,label):
        time.sleep(1)
        UI.alter_label(label,"3")
        time.sleep(1)
        UI.alter_label(label,"2")
        time.sleep(1)
        UI.alter_label(label,"1")
        time.sleep(1)
        label.destroy()

    def set_UI(self):
        self.hide_frames()
        self.root.configure(background='black')

        button = Button(self.root,text ="Begin",command = self.set_game)#threading.Thread(target=playGame).start)
        button.pack()

        button = Button(self.root,text ="Reset",command = self.set_UI)
        button.pack()

    def set_game(self):
        self.hide_frames()

        label = Label(text = "Type Statistics Game")
        label.pack()

        button = Button(self.root,text ="Reset",command = self.set_UI)
        button.pack()
        countdownLabel = Label(text = "3")
        countdownLabel.pack()
        start = threading.Thread(target=playGame,args=[countdownLabel])
        start.start()

    def set_phraseUI(self,text):
        label = Label(text = text)
        label.pack()

        self.inputLabel = Label(text = "")
        self.inputLabel.pack()
    
    def hide_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    ui = UI()
    ui.mainloop()
    cur.close()
    print("closed")



