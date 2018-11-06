

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