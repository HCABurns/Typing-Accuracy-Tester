#Imports
from Game import Game
#from UI import UI
from dbController import dbController
import threading
from UI import UI

class t:
    
    def __init__(self):
        self.ui = UI()
        self.ui.mainloop()

    def check(self):
        print(self.ui)

    def playGame():
        #global ui
        print(threading.active_count())
        main = Game()
        print(main.phrase)
        ui.set_phraseUI(main.phrase)
        ui.start_countdown()
        ui.setBind()
        main.begin()
        ui.unbind()
  
    

if __name__ == "__main__":
    from UI import UI
    global ui
    t()
    #ui = UI()
    #ui = UI()
    #ui.mainloop()
    print("")
    """
    g=5
    ui = UI()
    m.printa()
    ui.mainloop()
    """
    db = dbController()
    db.cur.close()
    print("closed")

