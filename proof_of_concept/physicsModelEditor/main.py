

# RECALL THE PATTERNS TO POTENTIALLY USE :
# 1. Abstract Factory pattern
# 2. Bridge pattern (strategy + adapter + structure)
# 3. Adapter pattern


# Resources of the physics engine
# Joints, Bodies, Actuators(if available)

class IJoint( object ) : # ADAPTER here, it seems

    # be careful with the constructor, as the wrappedjoint has no
    # an interface, but a concrete implementation from the engine. 
    # Perhaps could be passed to a setter when needed in construction
    def __init__( self, wrappedJoint ) :
        super( IJoint, self ).__init__()

        self.m_wrappedJoint = wrappedJoint

    # should not give access to the wrapped object. The ...
    # interface should do the job instead

    def setPosition( self ) :
        raise NotImplementedError( 'ERROR> IJoint::setPosition is pure virtual' )

    def getPosition( self ) :
        raise NotImplementedError( 'ERROR> IJoint::getPosition is pure virtual' )

    def setJointValue( self, value ) :
        raise NotImplementedError( 'ERROR> IJoint::setJointValue is pure virtual' )

    def getJointValue( self ) :
        raise NotImplementedError( 'ERROR> IJoint::getJointValue is pure virtual' )

    # maybe should expose a dictionary with abstract ...
    #  properties for the client to consume
    def getProps( self ) :
        raise NotImplementedError( 'ERROR> IJoint::getProps is pure virtual' )

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

# the factories

class IFactory( object ) :

    def __init__( self ) :
        super( IFactory, self ).__init__()

    # mmmm, here seems that the props should be a ...
    # very abstract dictionary/map, like map<Property> ...
    # where property is something from which we can ...
    # extract the data according to its type (like a wrapped property)
    # Adapter again?
    def createBody( self, props ) :
        raise NotImplementedError( 'ERROR> IFactory::createBody is pure virtual' )

    def createJoint( self, props ) :
        raise NotImplementedError( 'ERROR> IFactory::createJoint is pure virtual' )

    def createActuator( self, props ) :
        raise NotImplementedError( 'ERROR> IFactory::createActuator is pure virtual' )


class DartFactory( IFactory ) :

    def __init__( self ) :
        super( DartFactory, self ).__init__()

    def _createDartJointObj( self, props ) :
        return object()
        
    def createJoint( self, props ) :
        # create an actual dart joint
        _dartJointObj = self._createDartJointObj( props )
        # wrappe it with the DartJoint adapter
        _dartJoint = DartJoint( _dartJointObj )

        return _dartJoint
    
class BulletFactory( IFactory ) :

    def __init__( self ) :
        super( BulletFactory, self ).__init__()

    def _createBulletJointObj( self, props ) :
        return object()
    
    def createJoint( self, props ) :
        # create an actual bullet joint
        _bulletJointObj = self._createBulletJointObj( props )
        # wrappe it with the BulletJoint adapter
        _bullerJoint = BulletJoint( _bulletJointObj )

        return _bullerJoint

class MujocoFactory( IFactory ) :

    def __init__( self ) :
        super( MujocoFactory, self ).__init__()

    def _createMujocoJointObj( self, props ) :
        return object()
    
    def createJoint( self, props ) :
        # create an actual bullet joint
        _mujocoJointObj = self._createMujocoJointObj( props )
        # wrappe it with the BulletJoint adapter
        _mujocoJoint = MujocoJoint( _mujocoJointObj )

        return _mujocoJoint

class IEditor( object ) :

    def __init__( self, physicsHelper, rendererHelper ) :
        super( IEditor, self ).__init__()

        self.m_physicsHelper  = physicsHelper
        self.m_rendererHelper = rendererHelper

    