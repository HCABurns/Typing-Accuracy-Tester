#Imports
from tkinter import *
import threading
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
            time.sleep(1)
            #Load nunber 2 for 1 second.
            image = Image.open("images/2.png")
            num = ImageTk.PhotoImage(image)
            self.countdownLabel.config(image = num)
            time.sleep(1)
            #Load number 1 for 1 second.
            image = Image.open("images/1.png")
            num = ImageTk.PhotoImage(image)
            self.countdownLabel.config(image = num)
            time.sleep(1)
            #Remove the count down label
            self.countdownLabel.destroy()
        except:
            return -1

    def set_UI(self):
        """
        This function will set the window to the homescreen UI.
        """
        self.hide_frames()
        self.root.configure(background='black')
        bgColour = "black"

        #Add logo to the page
        image1 = Image.open("images/logo.png")
        logo = ImageTk.PhotoImage(image1)
        label = Label(image=logo, bg= bgColour, activebackground= bgColour)
        label.image=logo
        label.pack(pady=(20, 70))
        
        #Button to begin the game
        image2 = Image.open("images/startButton.png")
        startButton = ImageTk.PhotoImage(image2)
        label = Label(image=startButton, bg= bgColour, activebackground= bgColour)
        label.image=startButton
        button = Button(self.root,image=startButton,bd = 0,highlightbackground= bgColour, command = self.set_game,bg= bgColour, activebackground= bgColour, borderwidth=0)
        button.pack(pady=(0, 30))

        #Button to quit the game
        image3 = Image.open("images/exitButton.png")
        exitButton = ImageTk.PhotoImage(image3)
        label = Label(image=exitButton, bg= bgColour, activebackground= bgColour)
        label.image=exitButton
        button = Button(self.root,image=exitButton,bd = 0,highlightbackground= bgColour, command = self.close,bg= bgColour, activebackground= bgColour, borderwidth=0)
        button.pack()

    def set_game(self):
        """
        This function will start the countdown and create a new thread that will deal with the game code.
        """
        from main import playGame
        self.hide_frames()
        bgColour = "black"

        #Add logo to the page
        image1 = Image.open("images/logo.png")
        logo = ImageTk.PhotoImage(image1)
        label = Label(image=logo, bg= bgColour, activebackground= bgColour)
        label.image=logo
        label.pack(pady=(20, 40))

        #Add phrase label
        self.phraseLabel = Label(text = "", bg = bgColour, fg='#40a8e8', font="Helvetica 14 bold")
        self.phraseLabel.pack(pady=(0, 20))

        #Add countdown
        image1 = Image.open("images/3.png")
        num3 = ImageTk.PhotoImage(image1)
        self.countdownLabel = Label(image=num3, bg= bgColour, activebackground= bgColour)
        self.countdownLabel.image=num3
        self.countdownLabel.pack(pady=(0, 0))

        #Add input label
        self.inputLabel = Label(text = "", bg = bgColour, fg='#40a8e8', borderwidth = 2)
        self.inputLabel.pack(pady=(20, 0))

        #Button to quit the game
        image3 = Image.open("images/returnButton.png")
        exitButton = ImageTk.PhotoImage(image3)
        label = Label(image=exitButton, bg= bgColour, activebackground= bgColour)
        label.image=exitButton
        button = Button(self.root,image=exitButton,bd = 0,highlightbackground= bgColour, command = self.set_UI,bg= bgColour, activebackground= bgColour, borderwidth=0)
        button.place(x=self.width/2-(176/2),y=self.height-99)

        #Start a new thread to run the game. (Allows for this thread to continue to update the UI)
        self.thread = threading.Thread(target=playGame,args=[self.ui])
        self.thread.start()

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
        self.phraseLabel.config(text = text)

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
        sys.exit()

#Code for testing the UI class.
if __name__ == "__main__":
    ui = UI()
    ui.mainloop()


