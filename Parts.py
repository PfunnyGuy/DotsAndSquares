from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import ( QWidget, QLabel )


class Dot( QLabel ):
  # Constructor
  def __init__( self ):
    QLabel.__init__( self )
    self.setFixedSize( 5, 5 )
    self.setStyleSheet( "QLabel{ background-color: red }" )


class Line( QLabel ):
  wasClicked = pyqtSignal()

  # Constructor
  def __init__( self ):
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
    self.wasClicked.emit()
    self.setStyleSheet( "QLabel { background-color: black }" )


class HLine( Line ):
  # Constructor
  def __init__( self ):
    Line.__init__( self )
    self.setFixedSize( 20, 5 )


class VLine( Line ):
  # Constructor
  def __init__( self ):
    Line.__init__( self )
    self.setFixedSize( 5, 20 )


class Box( QLabel ):
  # Constructor
  def __init__( self ):
    QLabel.__init__( self )
    self.setFixedSize( 20, 20 )
    self.setStyleSheet( "QLabel{ background-color: yellow }" )
    self.topClicked    = False
    self.bottomClicked = False
    self.leftClicked   = False
    self.rightClicked  = False

  def SetTopClicked( self ):
    self.topClicked = True
    self.checkIfAllClicked()

  def SetBottomClicked( self ):
    self.bottomClicked = True
    self.checkIfAllClicked()

  def SetLeftClicked( self ):
    self.leftClicked   = True
    self.checkIfAllClicked()

  def SetRightClicked( self ):
    self.rightClicked  = True
    self.checkIfAllClicked()

  def checkIfAllClicked( self ):
    if( self.rightClicked and self.leftClicked and self.topClicked and self.bottomClicked ):
      self.setStyleSheet( "QLabel{ background-color: blue }" )

