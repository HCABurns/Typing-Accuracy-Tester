from tkinter import *
import threading
import time
#from main import playGame

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

    def start_countdown(self):
        time.sleep(1)
        UI.alter_label(self.countdownLabel,"3")
        time.sleep(1)
        UI.alter_label(self.countdownLabel,"2")
        time.sleep(1)
        UI.alter_label(self.countdownLabel,"1")
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
        #from tester import start2
        import tester
        self.hide_frames()

        label = Label(text = "Type Statistics Game")
        label.pack()

        button = Button(self.root,text ="Reset",command = self.set_UI)
        button.pack()
        self.countdownLabel = Label(text = "3")
        self.countdownLabel.pack()
        tester.start2()
        #start = threading.Thread(target=start)
        #start.start()

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
