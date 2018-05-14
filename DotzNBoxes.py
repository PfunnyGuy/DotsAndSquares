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


class DotzNBoxes( QWidget ):
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

    # TEST CODE - delete before final delivery.
    vl1 = VLine()
    vl2 = VLine()
    hl1 = HLine()
    hl2 = HLine()
    b1  = Box()
    r0  = QHBoxLayout()
    r1  = QHBoxLayout()
    r2  = QHBoxLayout()
    bigL = QVBoxLayout()

    r0.setSpacing( 0 )
    r1.setSpacing( 0 )
    r2.setSpacing( 0 )
    bigL.setSpacing( 0 )

    r0.addWidget( Dot() )
    r0.addWidget( hl1 )
    r0.addWidget( Dot() )
    r0.addStretch()

    r1.addWidget( vl1 )
    r1.addWidget( b1 )
    r1.addWidget( vl2 )
    r1.addStretch()

    r2.addWidget( Dot() )
    r2.addWidget( hl2 )
    r2.addWidget( Dot() )
    r2.addStretch()

    bigL.addLayout( r0 )
    bigL.addLayout( r1 )
    bigL.addLayout( r2 )
    bigL.addStretch()

    scorebox.addLayout( bigL )

    hl1.wasClicked.connect( b1.SetTopClicked )
    hl2.wasClicked.connect( b1.SetBottomClicked )
    vl1.wasClicked.connect( b1.SetLeftClicked )
    vl2.wasClicked.connect( b1.SetRightClicked )
    # END TEST CODE

    scorebox.addStretch()

    # add controls to the third row
    quitButton = QPushButton( "Quit" )
    quitButton.clicked.connect( self.HandleQuitButtonClick )

    row2.addWidget( QPushButton( "New Game" ) )
    row2.addStretch()
    row2.addWidget( quitButton )

    # TEST CODE - delete before final delivery.
    row2.addWidget( Dot() )
    row2.addWidget( VLine() )
    row2.addWidget( HLine() )
    row2.addWidget( Box() )
    # END TEST CODE

  def HandleQuitButtonClick( self ):
    QApplication.quit()

