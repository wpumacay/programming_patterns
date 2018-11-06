
from physicsModelEditor.core.IJoint import *

class DartJoint( IJoint ) :

    def __init__( self, wrappedJoint ) :
        super( DartJoint, self ).__init__( wrappedJoint )

    def setPosition( self ) :
        pass

    def getPosition( self ) :
        pass

    def setJointValue( self ) :
        pass

    def getProps( self ) :
        pass