

############################
#     Flying behaviours
############################

class FlyBehaviour( object ) :

    def __init__( self ) :
        self.m_behaviourName = 'BaseFlyBehaviour'

    # execute behaviour and return height delta
    def run( self ) :
        pass


class FlyWithWings( FlyBehaviour ) :

    def __init__( self ) :
        super( FlyWithWings, self ).__init__()

        self.m_behaviourName = 'FlyWithWingsBehaviour'

    def run( self ) :
        return 2.0

class FlyWithBarrelRoll( FlyBehaviour ) :

    def __init__( self ) :
        super( FlyWithBarrelRoll, self ).__init__()

        self.m_behaviourName = 'FlyWithBarrelRoll'

    def run( self ) :
        return 10.0

class FlyWithUTurn( FlyBehaviour ) :

    def __init__( self ) :
        super( FlyWithUTurn, self ).__init__()

        self.m_behaviourName = 'FlyWithUTurn'

    def run( self ) :
        return 5.0

class FlyNoWay( FlyBehaviour ) :

    def __init__( self ) :
        super( FlyNoWay, self ).__init__()

    def run( self ) :
        return 0.0


############################
#    Quacking behaviours
############################

class QuackBehaviour( object ) :

    def __init__( self ) :
        pass

class QuackNormal( QuackBehaviour ) :

    def __init__( self ) :
        super( QuackNormal, self ).__init__()

    def run( self ) :
        print( 'Quack!!!, I am a duck' )

class QuackSqueak( QuackBehaviour ) :

    def __init__( self ) :
        super( QuackSqueak, self ).__init__()

    def run( self ) :
        print( 'Squeak, a plastic sound' )

class QuackLikePeppy( QuackBehaviour ) :

    def __init__( self ) :
        super( QuackLikePeppy, self ).__init__()

    def run( self ) :
        print( 'DO A BARREL ROLL!!!' )

class QuackMute( QuackBehaviour ) :

    def __init__( self ) :
        super( QuackMute, self ).__init__()

    def run( self ):
        # does nothing - no quack
        pass

############################
#   Duck core container
############################

class Duck( object ) :

    def __init__( self ) :
        self.m_height = 0.0

        # behaviours for fly and quack ...
        # (extracted from the core container)
        self.m_flyBehaviour = None
        self.m_quackBehaviour = None

    def fly( self ) :
        if self.m_flyBehaviour is not None :
            self.m_height += self.m_flyBehaviour.run()
    
    def quack( self ) :
        if self.m_quackBehaviour is not None :
            self.m_quackBehaviour.run()

    def height( self ) : 
        return self.m_height

class StarFoxDuck( Duck ) :

    def __init__( self ) :
        super( StarFoxDuck, self ).__init__()

        self.m_flyBehaviour = FlyWithBarrelRoll()
        self.m_quackBehaviour = QuackLikePeppy()

class SimpleDuck( Duck ) :

    def __init__( self ) :
        super( SimpleDuck, self ).__init__()

        self.m_flyBehaviour = FlyWithWings()
        self.m_quackBehaviour = QuackNormal()
