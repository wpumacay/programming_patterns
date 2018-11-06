
from physicsModelEditor.core.IJoint import *

class MujocoJoint( IJoint ) :

    def __init__( self, wrappedJoint ) :
        super( MujocoJoint, self ).__init__( wrappedJoint )

    def setPosition( self ) :
        pass

    def getPosition( self ) :
        pass

    def setJointValue( self ) :
        pass

    def getProps( self ) :
        pass