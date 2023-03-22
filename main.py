#Imports
from Game import Game
from DBController import DBController
import threading
from UI import UI
import sys

    
#Open a database connect and make it global
global db
db = DBController()

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
    print(threading.active_count()) 
    main = Game(ui,db)
    ui.set_phraseUI(main.phrase)
    ui.start_countdown()
    ui.setBind()
    results = main.begin()
    print(results)
    ui.unbind()
    try:
        if len(results) == 0:
            ui.set_UI()
        else:
            ui.set_results_UI(results[0],results[1],results[2],results[3])
    except:
        return -1

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

    

