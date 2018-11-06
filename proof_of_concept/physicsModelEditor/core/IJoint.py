

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