#Imports
from Game import Game
from dbController import dbController
import threading
from UI import UI
import sys

    
#Open a database connect and make it global
global db
db = dbController()

def playGame(ui):
    """
    This function is used to start the game.

    Parameters
    --------------
    ui - UI Class object
        This is a object of the UI that has been passed by refernce to the
        UI class.

    Return
    --------------
    None
    """
    main = Game(ui,db)
    ui.set_phraseUI(main.phrase)
    ui.start_countdown()
    ui.setBind()
    g = main.begin()
    print(g)
    ui.unbind()
    

if __name__ == "__main__":
    #Open UI
    ui = UI()
    #Set the UI parameter to the ui object
    ui.ui = ui
    #Mainloop 
    ui.mainloop()
    #When the UI is closed, close the database connection.
    #db = dbController()
    db.cur.close()
    print("closed")
    sys.exit()

    

