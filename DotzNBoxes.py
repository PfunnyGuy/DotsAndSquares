from PyQt5.QtWidgets import ( QApplication, 
															QWidget, 
															QGroupBox,
															QPushButton,
															QLabel,
															QHBoxLayout,
															QVBoxLayout )


class DotzNBoxes( QWidget ):
	def __init__( self ):
		QWidget.__init__( self )
		
		# Make the pieces of the class:
		# Set up the pieces for game app.  It needs an app, the app
		# needs a widget, and the widget needs a layout
		gameLayout = QVBoxLayout()

		self.setLayout( gameLayout )
		self.setWindowTitle( "Dotz - N - Boxes" )
		
		self.move( 300, 300 )			 # Set the position of the window
		
		
		# My game will have an overall layout of 3 rows to hold the 
		# controls.  These are the rows:
		row0 = QHBoxLayout()
		row1 = QHBoxLayout()
		row2 = QHBoxLayout()
		
		# Add the rows to the layout 
		gameLayout.addLayout( row0 )
		gameLayout.addLayout( row1 )
		gameLayout.addLayout( row2 )
		
		# add controls to the first row
		turnLabel = QLabel( "Red Player: It's your turn!" )
		turnLabel.setMaximumHeight( 25 )
		row0.addWidget( turnLabel )
		
		# add controls to the second row
		gameBoard = QGroupBox( "" )
		gameBoard.setFixedSize( 500, 500 )
		row1.addWidget( gameBoard )
		
		# the score will be in a column to the right of the
		# game board.  Create a box and add the score to
		# it.
		scorebox = QVBoxLayout()
		row1.addLayout(scorebox)
		
		scorebox.addWidget( QLabel("Score") )
		scorebox.addWidget( QLabel("Blue : 0") )
		scorebox.addWidget( QLabel("Red  : 0") )
		scorebox.addStretch()
		
		# add controls to the third row
		row2.addWidget( QPushButton( "New Game" ) )
		row2.addStretch()
		row2.addWidget( QPushButton( "Quit" ) )
