from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import ( QApplication,
                              QWidget,
                              QGroupBox,
                              QPushButton,
                              QLabel,
                              QHBoxLayout,
                              QVBoxLayout )
from Parts import Dot
from Parts import VLine
from Parts import HLine
from Parts import Box

BOARD_SIZE = 5
PLAYER_1 = "Blue"
PLAYER_2 = "Red"


class DotzNBoxes( QWidget ):
  changeColor = pyqtSignal()

  # Constructor
  def __init__( self ):
    # DotzNBoxes is a QWidget, so I need to call the constructor for QWidget
    # to initialize that part of DotzNBoxes.
    QWidget.__init__( self )

    # Make the pieces of the class:
    # Set up the pieces for game app.  It needs an app, the app
    # needs a widget, and the widget needs a layout
    gameLayout = QVBoxLayout()

    self.setLayout( gameLayout )
    self.setWindowTitle( "Dotz - N - Boxes" )
    self.move( 300, 300 )      # Set the position of the window
    self.playersTurn = PLAYER_1
    self.P1score = 0
    self.P2score = 0
    self.scored = False

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
    self.turnLabel = QLabel( PLAYER_1 + " Player: It's your turn!" )
    self.turnLabel.setMaximumHeight( 25 )
    row0.addWidget( self.turnLabel )

    # add controls to the second row
    # First, create the board for the game
    boardLayout = QVBoxLayout()
    boardLayout.addStretch()
    boardLayout.setSpacing( 0 )

    boxes  = [[Box()   for r in range( BOARD_SIZE    )] for c in range( BOARD_SIZE    )]
    hlines = [[HLine() for r in range( BOARD_SIZE    )] for c in range( BOARD_SIZE + 1)]
    vlines = [[VLine() for r in range( BOARD_SIZE + 1)] for c in range( BOARD_SIZE    )]

    for row in range( BOARD_SIZE ):
      lineLayout = QHBoxLayout()
      lineLayout.addStretch()
      lineLayout.setSpacing( 0 )
      boxLayout = QHBoxLayout()
      boxLayout.addStretch()
      boxLayout.setSpacing( 0 )
      boardLayout.addLayout( lineLayout )
      boardLayout.addLayout( boxLayout )

      for column in range( BOARD_SIZE ):
        lineLayout.addWidget( Dot() )
        lineLayout.addWidget( hlines[row][column] )
        boxLayout.addWidget( vlines[row][column] )
        boxLayout.addWidget( boxes[row][column] )

        hlines[row  ][column  ].wasClicked.connect( boxes[row][column].SetTopClicked )
        hlines[row+1][column  ].wasClicked.connect( boxes[row][column].SetBottomClicked )
        vlines[row  ][column  ].wasClicked.connect( boxes[row][column].SetLeftClicked )
        vlines[row  ][column+1].wasClicked.connect( boxes[row][column].SetRightClicked )

        hlines[row][column].changedColor.connect( self.ChangePlayerTurn )
        vlines[row][column].changedColor.connect( self.ChangePlayerTurn )

        boxes[row][column].completed.connect( self.SomeoneScored )
        self.changeColor.connect( boxes[row][column].ChangeColor )

      lineLayout.addWidget( Dot() )
      boxLayout.addWidget( vlines[row][BOARD_SIZE] )
      vlines[row][BOARD_SIZE].changedColor.connect( self.ChangePlayerTurn )

      lineLayout.addStretch()
      boxLayout.addStretch()

    # Add final lineLayout, to "Cap" the bottom of the boardLayout
    lineLayout = QHBoxLayout()
    lineLayout.addStretch()
    lineLayout.setSpacing( 0 )
    for column in range( BOARD_SIZE ):
      lineLayout.addWidget( Dot() )
      lineLayout.addWidget( hlines[BOARD_SIZE][column] )
      hlines[BOARD_SIZE][column].changedColor.connect( self.ChangePlayerTurn )

    lineLayout.addWidget( Dot() )
    lineLayout.addStretch()
    boardLayout.addLayout( lineLayout )

    boardLayout.addStretch()

    # Make a box around the game.
    boardFrame = QGroupBox( "" )
    boardFrame.setFixedSize( 500, 500 )
    boardFrame.setLayout( boardLayout )
    row1.addWidget( boardFrame )

    # the score will be in a column to the right of the
    # game board.  Create a box and add the score to
    # it.
    scorebox = QVBoxLayout()
    self.scoreLabel1 = QLabel(PLAYER_1 + " : 0")
    self.scoreLabel2 = QLabel( PLAYER_2 + " : 0" )

    row1.addLayout(scorebox)

    scorebox.addWidget( QLabel("Score") )
    scorebox.addWidget( self.scoreLabel1 )
    scorebox.addWidget( self.scoreLabel2 )

    scorebox.addStretch()

    # add controls to the third row
    quitButton = QPushButton( "Quit" )
    quitButton.clicked.connect( self.HandleQuitButtonClick )

    row2.addWidget( QPushButton( "New Game" ) )
    row2.addStretch()
    row2.addWidget( quitButton )


  def HandleQuitButtonClick( self ):
    QApplication.quit()

  def ChangePlayerTurn( self ):
    if( self.scored == True ):
      self.scored = False
    else:
      if( self.playersTurn == PLAYER_1 ):
        self.playersTurn = PLAYER_2
      else:
        self.playersTurn = PLAYER_1
      self.turnLabel.setText( self.playersTurn + " Player: It's your turn!" )
      self.changeColor.emit()

  def SomeoneScored( self ):
    self.scored = True
    if( self.playersTurn == PLAYER_1 ):
      self.P1score = self.P1score + 1
      self.scoreLabel1.setText(PLAYER_1 + " : " + str( self.P1score ) )
    else:
      self.P2score = self.P2score + 1
      self.scoreLabel2.setText( PLAYER_2 + " : " + str( self.P2score ) )

