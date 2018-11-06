
from physicsModelEditor.core.IJoint import *

class BulletJoint( IJoint ) :

    def __init__( self, wrappedJoint ) :
        super( BulletJoint, self ).__init__( wrappedJoint )

    def setPosition( self ) :
        pass

    def getPosition( self ) :
        pass

    def setJointValue( self ) :
        pass

    def getProps( self ) :
        pass