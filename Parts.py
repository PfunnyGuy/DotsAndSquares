from PyQt5.QtWidgets import ( QWidget, QLabel )


class Dot( QLabel ):
  # Constructor
  def __init__( self ):
    # DotzNBoxes is a QWidget, so I need to call the constructor for QWidget
    # to initialize that part of DotzNBoxes.
    QLabel.__init__( self )
    self.setFixedSize( 5, 5 )
    self.setStyleSheet( "QLabel{ background-color: red }" )


class Line( QLabel ):
  # Constructor
  def __init__( self ):
    # DotzNBoxes is a QWidget, so I need to call the constructor for QWidget
    # to initialize that part of DotzNBoxes.
    QLabel.__init__( self )
    self.setStyleSheet( "QLabel{ background-color: white }" )
    self.hasBeenClicked = False

  def enterEvent( self, event ):
    if( not self.hasBeenClicked ):
      self.setStyleSheet( "QLabel { background-color: gray }" )

  def leaveEvent( self, event ):
    if( not self.hasBeenClicked ):
      self.setStyleSheet( "QLabel { background-color: white }" )

  def  mousePressEvent(self, event):
    self.hasBeenClicked = True
    self.setStyleSheet( "QLabel { background-color: black }" )


class HLine( Line ):
  # Constructor
  def __init__( self ):
    # DotzNBoxes is a QWidget, so I need to call the constructor for QWidget
    # to initialize that part of DotzNBoxes.
    Line.__init__( self )
    self.setFixedSize( 20, 5 )


class VLine( Line ):
  # Constructor
  def __init__( self ):
    # DotzNBoxes is a QWidget, so I need to call the constructor for QWidget
    # to initialize that part of DotzNBoxes.
    Line.__init__( self )
    self.setFixedSize( 5, 20 )


class Box( QLabel ):
  # Constructor
  def __init__( self ):
    # DotzNBoxes is a QWidget, so I need to call the constructor for QWidget
    # to initialize that part of DotzNBoxes.
    QLabel.__init__( self )
    self.setFixedSize( 25, 25 )
    self.setStyleSheet( "QLabel{ background-color: yellow }" )
    self.topClicked    = False
    self.bottomClicked = False
    self.leftClicked   = False
    self.rightClicked  = False
