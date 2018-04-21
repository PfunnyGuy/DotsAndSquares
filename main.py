#!C:\Python36\python.exe

import sys 

from DotzNBoxes import DotzNBoxes

from PyQt5.QtWidgets import ( QApplication )


# Set up the pieces for game app.  It needs an app, the app
# needs a widget, and the widget needs a layout
myGameApp  = QApplication( sys.argv )
myGame     = DotzNBoxes() #QWidget()

# Done building the game.  Let's play!
myGame.show()
sys.exit( myGameApp.exec_() )
