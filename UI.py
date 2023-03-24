#Imports
from tkinter import *
from tkinter import messagebox
import threading
from DBController import DBController
import time
import sys
from PIL import ImageTk, Image

class UI():
    """
    This is the class to deal with the Tkinter UI code.

    Methods
    ---------------
    __init__() - Creates a window with correct geometry, title and logo.
    setBind() - This binds a keyboard input to run a function. (Disabled before game)
    unbind() -Unbinds the keyboard input that runs a function.
    key_press(event) - Uses the event to find which key was entered and add/remove a char
                       from the users input.
    alter_label(label,newText) - Change the text of a label to newText. 
    start_countdown() - Creates a label with a countdown (3->2->1) then destroys the label.
    set_UI() - Set the UI of the homescreen.
    set_game() - Set the UI of the game screen.
    set_phraseUI(text) - Creates the UI for the phrase and input.
    hide_frames() - Remove all frames currently on the window.
    mainloop() - Runs mainloop on the window.
    """
    def __init__(self):
        """
        Creates a window.
        """
        self.root = Tk()
        self.width = 800
        self.height = 400
        self.root.geometry("{}x{}".format(self.width, self.height))
        self.root.title("Typing Speed Calculator")
        self.root.iconphoto(False, PhotoImage(file='images/icon.png'))
        self.bgColour = "black"
        self.root.configure(background=self.bgColour)
        self.set_UI()
        self.ui = None


    def setBind(self):
        """
        This function binds any key press event to run the key_press function.
        """
        self.root.bind('<Key>', self.ui.key_press)
        

    def unbind(self):
        """
        This function unbinds any key press event.
        """
        self.root.unbind('<Key>')


    def key_press(self,event):
        """
        This function will either add or remove a character to the user input label.

        Parameters
        -----------------
        event : KeyPress event
            This occurs when the user presses any key.
        """
        if event.keysym == "BackSpace":
            self.inputLabel.config(text="{}".format(self.inputLabel.cget("text")[:-1]))
        else:
            self.inputLabel.config(text="{}".format(self.inputLabel.cget("text") + event.char))


    def alter_label(label,newText):
        """
        This function will update the text in a given label.

        Parameters
        -----------------
        label : tkitner label
            This is the label that will be changed.
        newText : string
            This is the new text that will replace the old text in the label.
        """
        label.config(text = newText)


    def start_countdown(self):
        """
        This function will change the countdown and wait 3 seconds before starting the game.
        """
        try:
            #Sleep for 1 second to allow for 3 to be on screen.
            #time.sleep(1)
            
            #Load nunber 2 for 1 second.
            image = Image.open("images/2.png")
            num = ImageTk.PhotoImage(image)
            self.countdownLabel.config(image = num)
            #time.sleep(1)
            
            #Load number 1 for 1 second.
            image = Image.open("images/1.png")
            num = ImageTk.PhotoImage(image)
            self.countdownLabel.config(image = num)
            #time.sleep(1)
            
            #Remove the count down label
            self.returnButton["state"] = NORMAL
            self.countdownLabel.destroy()   
        except:
            return -1


    def set_UI(self):
        """
        This function will set the window to the homescreen UI.
        """
        self.hide_frames()

        #Add logo to the page
        image1 = Image.open("images/logo.png")
        logo = ImageTk.PhotoImage(image1)
        label = Label(image=logo, bg= self.bgColour, activebackground= self.bgColour)
        label.image=logo
        label.pack(pady=(20, 20))
        
        #Button to begin the game
        image2 = Image.open("images/startButton.png")
        startButton = ImageTk.PhotoImage(image2)
        label = Label(image=startButton, bg= self.bgColour, activebackground= self.bgColour)
        label.image=startButton
        button = Button(self.root,image=startButton,bd = 0,highlightbackground= self.bgColour, command = self.set_game,bg= self.bgColour, activebackground=self.bgColour, borderwidth=0)
        button.pack(pady=(0, 15))

        #Button to go to leaderboards
        image3 = Image.open("images/leaderboardButton.png")
        exitButton = ImageTk.PhotoImage(image3)
        label = Label(image=exitButton, bg= self.bgColour, activebackground= self.bgColour)
        label.image=exitButton
        button = Button(self.root,image=exitButton,bd = 0,highlightbackground= self.bgColour, command = self.show_leaderboard,bg= self.bgColour, activebackground= self.bgColour, borderwidth=0)
        button.pack(pady=(0,15))

        #Button to quit the game
        image3 = Image.open("images/exitButton.png")
        exitButton = ImageTk.PhotoImage(image3)
        label = Label(image=exitButton, bg= self.bgColour, activebackground= self.bgColour)
        label.image=exitButton
        button = Button(self.root,image=exitButton,bd = 0,highlightbackground= self.bgColour, command = self.close,bg= self.bgColour, activebackground= self.bgColour, borderwidth=0)
        button.pack()


    def set_game(self):
        """
        This function will start the countdown and create a new thread that will deal with the game code.
        """
        from main import playGame
        self.hide_frames()

        #Add logo to the page
        image1 = Image.open("images/logo.png")
        logo = ImageTk.PhotoImage(image1)
        label = Label(image=logo, bg= self.bgColour, activebackground=self.bgColour)
        label.image=logo
        label.pack(pady=(20, 40))

        #Add phrase label
        self.phraseLabel = Label(text = "", bg =self.bgColour, fg='#40a8e8', font="Helvetica 14 bold",wraplength=self.width-50)
        self.phraseLabel.pack(pady=(0, 20))

        #Add countdown
        image1 = Image.open("images/3.png")
        num3 = ImageTk.PhotoImage(image1)
        self.countdownLabel = Label(image=num3, bg= self.bgColour, activebackground= self.bgColour)
        self.countdownLabel.image=num3
        self.countdownLabel.pack(pady=(0, 0))

        #Add input label
        self.inputLabel = Label(text = "", bg = self.bgColour, fg='#40a8e8', borderwidth = 2)
        self.inputLabel.pack(pady=(20, 0))

        #Button to return
        image3 = Image.open("images/returnButton.png")
        exitButton = ImageTk.PhotoImage(image3)
        label = Label(image=exitButton, bg= self.bgColour, activebackground= self.bgColour)
        label.image=exitButton
        self.returnButton = Button(self.root,image=exitButton,bd = 0,highlightbackground= self.bgColour, command = self.set_UI,bg=self.bgColour, activebackground= self.bgColour, borderwidth=0)
        self.returnButton.place(x=self.width/2-(176/2),y=self.height-99)
        self.returnButton["state"] = DISABLED

        #Start a new thread to run the game. (Allows for this thread to continue to update the UI)
        self.thread = threading.Thread(target=playGame,args=[self.ui])
        self.thread.start()


    def set_results_UI(self,accuracy,time,wpm,accurate_wpm,score):
        """
        This function will set the window to the homescreen UI.
        """
        self.hide_frames()

        #Add logo to the page
        image1 = Image.open("images/logo.png")
        logo = ImageTk.PhotoImage(image1)
        label = Label(image=logo, bg= self.bgColour, activebackground=self.bgColour)
        label.image=logo
        label.pack(pady=(20, 0))

        #Add accuracy label
        label = Label(text = f"Completed in {round(time,2)}s with accuracy of: {round(accuracy,2)}%", bg = self.bgColour, fg='#40a8e8', borderwidth = 2, font="Helvetica 14 bold")
        label.pack(pady=(20, 0))

        #Add wpm label
        label = Label(text = f"Words per minute (WPM) of: {round(wpm,2)}", bg = self.bgColour, fg='#40a8e8', borderwidth = 2, font="Helvetica 14 bold")
        label.pack(pady=(20, 0))

        #Add accurate wpm label
        label = Label(text = f"Accurate words per minute (WPM) of: {round(accurate_wpm,2)}", bg = self.bgColour, fg='#40a8e8', borderwidth = 2, font="Helvetica 14 bold")
        label.pack(pady=(20, 0))

        #Add score label
        label = Label(text = f"Total Score: {score}", bg =self.bgColour, fg='#40a8e8', borderwidth = 2, font="Helvetica 14 bold")
        label.pack(pady=(20, 20))

        w = Frame(bg=self.bgColour)
        w.pack()
        
        #Button to return
        image3 = Image.open("images/returnButton.png")
        exitButton = ImageTk.PhotoImage(image3)
        label = Label(image=exitButton, bg= self.bgColour, activebackground= self.bgColour)
        label.image=exitButton
        button = Button(w,image=exitButton,bd = 0,highlightbackground= self.bgColour, command = self.set_UI,bg= self.bgColour, activebackground= self.bgColour, borderwidth=0)
        button.grid(row=0,column=2)

        l = Label(w, text = "         ", bg = self.bgColour)
        l.grid(row = 0, column = 1)

        #Button to go to leaderboards
        image3 = Image.open("images/leaderboardButton.png")
        exitButton = ImageTk.PhotoImage(image3)
        label = Label(image=exitButton, bg= self.bgColour, activebackground= self.bgColour)
        label.image=exitButton
        button = Button(w,image=exitButton,bd = 0,highlightbackground= self.bgColour, command = lambda: self.set_leaderboard_UI(score),bg= self.bgColour, activebackground= self.bgColour, borderwidth=0)
        button.grid(row=0,column=0)


    def set_leaderboard_UI(self,score):
        """
        This function will set the dispaly to let the user enter the details to submit their score to the leaderboard.
        """

        self.hide_frames()

        #Add logo to the page
        image1 = Image.open("images/logo.png")
        logo = ImageTk.PhotoImage(image1)
        label = Label(image=logo, bg= self.bgColour, activebackground= self.bgColour)
        label.image=logo
        label.pack(pady=(20, 0))
    
        #Add Name label and entry box
        frame1 = Frame(self.root, bg= "black")
        frame1.pack()
        label = Label(frame1,text = "Identifier: ", bg = self.bgColour, fg='#40a8e8', font="Helvetica 20 bold")
        entry = Entry(frame1, fg='#40a8e8',width=5)
        label.grid(row = 0 , column = 0,sticky="e")
        entry.grid(row = 0 , column = 2)

        #Add the score
        label = Label(frame1,text = f"Score: ", bg = self.bgColour, fg='#40a8e8', font="Helvetica 20 bold")
        label.grid(row = 1, column = 0,sticky="e")
        label = Label(frame1,text = f"{score}", bg = self.bgColour, fg='#40a8e8', font="Helvetica 20 bold")
        label.grid(row = 1, column = 2, sticky = "w")

        #Error label
        self.errorLabel = Label(text = "", bg = self.bgColour, fg='#ff002b', font="Helvetica 14 bold")
        self.errorLabel.pack()
        #Button to submit
        image3 = Image.open("images/submitButton.png")
        exitButton = ImageTk.PhotoImage(image3)
        label = Label(image=exitButton, bg= self.bgColour, activebackground= self.bgColour)
        label.image=exitButton
        button = Button(self.root,image=exitButton,bd = 0,highlightbackground= self.bgColour, command = lambda: self.info_checker(entry.get(),score),bg= self.bgColour, activebackground= self.bgColour, borderwidth=0)
        button.pack(pady=(20,0))


    def info_checker(self, identifier,score):
        """
        This function will check that the name the user enters is valid.

        Parameters
        --------------
        identifier : string
            This is the identifier the user has entered to represent them.
        """
        if len(identifier) == 3:
            identifier = identifier.upper()
            db = DBController()
            print(self.phrase)
            command = f'SELECT id FROM Phrases WHERE phrase="{self.phrase}"'
            print(command)
            phraseID = db.cur.execute(command)
            phraseID = db.cur.fetchall()[0][0]
            print(phraseID)
            command = f"INSERT INTO Scores(name, score, phraseID) VALUES ('{identifier}', {score}, {phraseID});"
            print(command)
            db.execute(command)
            db.commit()
            self.show_leaderboard(identifier,score)
        else:
            self.errorLabel.config(text = "ERROR: The identifier must be exactly 3 characters long!")
            #messagebox.showerror('Error', 'field must contain 3 characters')


    def show_leaderboard(self,name=None,score=None):
        """
        This fuction is used to display a leaderboard of the top X scores.

        Parameter
        ------------
        name : str
            This is the users identifier they entered.
            Set to None by default as this is relevant for showing the last users score.

        score : str
            This is the users score they achieved.
            Set to None by default as this is relevant for showing the last users score.

        """
        
        db = DBController()
        scores = db.getScores()
        scores.sort(key=lambda x: x[1],reverse=True)
        print(scores)
        self.hide_frames()
        
        #Add logo to the page
        image1 = Image.open("images/logo.png")
        logo = ImageTk.PhotoImage(image1)
        label = Label(image=logo, bg= self.bgColour, activebackground= self.bgColour)
        label.image=logo
        label.pack(pady=(10, 0))

        frame = Frame(self.root, bg = self.bgColour)
        frame.pack()

        #Add the top X scores
        for i in range(1,6):
            positionLabel = Label(frame, text = f"{i}. ", bg = self.bgColour, fg='#40a8e8', font="Helvetica 16 bold")
            nameLabel = Label(frame, text = scores[i-1][0]  + "  ", bg = self.bgColour, fg='#40a8e8', font="Helvetica 16 bold")
            scoreLabel = Label(frame, text = scores[i-1][1],bg = self.bgColour, fg='#40a8e8', font="Helvetica 16 bold")
            spacerLabel = Label(frame, text = "           ",bg = self.bgColour)

            positionLabel.grid(row = i, column = 0)
            nameLabel.grid(row = i, column = 1)
            scoreLabel.grid(row = i, column = 2, sticky = "W")
            spacerLabel.grid(row = i, column = 3)

        #Add the other side of the scoreboard
        for i in range(6,11):
            positionLabel = Label(frame, text = f"{i}. ", bg = self.bgColour, fg='#40a8e8', font="Helvetica 16 bold")
            nameLabel = Label(frame, text = scores[i-1][0]  + "  ", bg = self.bgColour, fg='#40a8e8', font="Helvetica 16 bold")
            scoreLabel = Label(frame, text = scores[i-1][1],bg = self.bgColour, fg='#40a8e8', font="Helvetica 16 bold")

            positionLabel.grid(row = i-5, column = 4)
            nameLabel.grid(row = i-5, column = 5)
            scoreLabel.grid(row = i-5, column = 6, sticky = "W")


        #ADd the previous score - If possible
        if name is not None:
            for i,nameAndScore in enumerate(scores):
                if nameAndScore[0]==name and nameAndScore[1] == score:
                    pos = i+1
                    break     
            positionLabel = Label(frame, text = f"{pos}. ", bg = self.bgColour, fg='#40a8e8', font="Helvetica 16 bold")
            nameLabel = Label(frame, text = name.upper() + "  ", bg = self.bgColour, fg='#40a8e8', font="Helvetica 16 bold")
            scoreLabel = Label(frame, text = score,bg = self.bgColour, fg='#40a8e8', font="Helvetica 16 bold")
            spacerLabel.grid(row = 11, column = 3)
            positionLabel.grid(row = 12, column = 2, sticky= "E")
            nameLabel.grid(row = 12, column = 3, sticky= "W")
            scoreLabel.grid(row = 12, column = 4, sticky = "W")

        #Button to return
        image3 = Image.open("images/returnButton.png")
        exitButton = ImageTk.PhotoImage(image3)
        label = Label(image=exitButton, bg= self.bgColour, activebackground= self.bgColour)
        label.image=exitButton
        button = Button(self.root,image=exitButton,bd = 0,highlightbackground= self.bgColour, command = self.set_UI,bg= self.bgColour, activebackground= self.bgColour, borderwidth=0)
        button.pack(pady=(10,0))
    
    def returnButton(self):
        """
        This function is to end the game
        """
        self.thread.join()
        self.unbind()
        self.set_UI()
    

    def set_phraseUI(self,text):
        """
        This function will set the UI for the phrase and input.

        Parameters
        --------------
        text : string
            This is the phrase the game chose from the database.
        """
        bgColour = "black"
        self.phrase = text
        self.phraseLabel.config(text = self.phrase)

        #self.inputLabel = Label(text = "", bg = bgColour, fg='#40a8e8')
        #self.inputLabel.pack()
    
    def hide_frames(self):
        """
        This function will destroy everything in the window.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

    def mainloop(self):
        """
        This function runs the required mainloop for the window.
        """
        self.root.mainloop()


    def close(self):
        """
        This function is used to close the window and end the program.
        """
        self.root.destroy()


#Code for testing the UI class.
if __name__ == "__main__":
    ui = UI()
    ui.mainloop()


