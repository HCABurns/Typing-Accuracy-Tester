from tkinter import *
import threading
import time

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
        self.root.geometry("{}x{}".format(800, 480))
        self.root.title("Typing Speed Calculator")
        self.root.iconphoto(False, PhotoImage(file='logo.png'))
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
        time.sleep(1)
        UI.alter_label(self.countdownLabel,"3")
        time.sleep(1)
        UI.alter_label(self.countdownLabel,"2")
        time.sleep(1)
        UI.alter_label(self.countdownLabel,"1")
        time.sleep(1)
        self.countdownLabel.destroy()

    def set_UI(self):
        """
        This function will set the window to the homescreen UI.
        """
        self.hide_frames()
        self.root.configure(background='black')

        button = Button(self.root,text ="Begin",command = self.set_game)
        button.pack()

        button = Button(self.root,text ="Reset",command = self.set_UI)
        button.pack()

    def set_game(self):
        """
        This function will start the countdown and create a new thread that will deal with the game code.
        """
        from main import playGame
        self.hide_frames()

        label = Label(text = "Type Statistics Game")
        label.pack()

        button = Button(self.root,text ="Reset",command = self.set_UI)
        button.pack()
        self.countdownLabel = Label(text = "3")
        self.countdownLabel.pack()

        #Start a new thread to run the game. (Allows for this thread to continue to update the UI)
        start = threading.Thread(target=playGame,args=[self.ui])
        start.start()

    def set_phraseUI(self,text):
        """
        This function will set the UI for the phrase and input.

        Parameters
        --------------
        text : string
            This is the phrase the game chose from the database.
        """
        label = Label(text = text)
        label.pack()

        self.inputLabel = Label(text = "")
        self.inputLabel.pack()
    
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

#Code for testing the UI class.
if __name__ == "__main__":
    ui = UI()
    ui.mainloop()


