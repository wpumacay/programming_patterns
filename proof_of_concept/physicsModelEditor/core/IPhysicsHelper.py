
from physicsModelEditor.core.IFactory import IFactory

class IPhysicsHelper( object ) :

    def __init__( self, factory ) :
        super( IPhysicsHelper, self ).__init__()
        # the factory to use to create the wrapped elements
        self.m_factory = factory
        # mmm, here it seems it should be the same wether the ...
        # helper has the actual wrapped elements or not. Another ...
        # option would be to store them in the factory, but will ...
        # keep them here as a first implementation
        self.m_bodies = {}
        self.m_joints = {}
        self.m_actuators = {} # These could be handled with the Null object pattern

    def getBodyByName( self, name ) :
        if name in self.m_bodies :
            return self.m_bodies[ name ]
        else :
            print( 'WARNING> requested body with name: ', 
                   name, ' is not in the bodies list' )
            return None

    def getJointByName( self, name ) :
        if name in self.m_joints :
            return self.m_joints[ name ]
        else :
            print( 'WARNING> requested joint with name: ', 
                   name, ' is not in the joints list' )
            return None

    def getActuatorByName( self, name ) :
        if name in self.m_actuators :
            return self.m_actuators[ name ]
        else :
            print( 'WARNING> requested actuator with name: ', 
                   name, ' is not in the actuators list' )
            return None

    def moveBodyElement( self, elName, elPosition ) :
        _body = self.getBodyByName( elName )
        if _body is None :
            return
        
        _body.setPosition( elPosition )

    # check needed API here. It seems more reasonable to ...
    # make the move method a relative-move instead (for joints)
    def moveJointElement( self, elName, elPosition ) :
        _joint = self.getJointByName( elName )
        if _joint is None :
            return

        _joint.setPosition( elPosition )

    def rotateElement( self, elName, elOrientation ) :
        pass

    def scaleElement( self, elName, elScale ) :
        pass

    def createBody( self, elName, props ) :
        _nbody = self.m_factory.createBody( props )
        self.m_bodies[ elName ] = _nbody
    
    def createJoint( self, elName, props ) :
        _njoint = self.m_factory.createJoint( props )
        self.m_joints[ elName ] = _njoint

    def createActuator( self, elName, props ) :
        _nactuator = self.m_factory.createActuator( props )
        self.m_actuators[ elName ] = _nactuator