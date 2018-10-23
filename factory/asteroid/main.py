



class GameObject( object ) :

    def __init__( self ) :
        super( GameObject, self ).__init__()

class GameWorld( object ) :

    def __init__( self ) :
        super( GameWorld, self ).__init__()

        self.m_gameObjs = []

    def addGameObject( self, gameObj ) :
        self.m_gameObjs.append( gameObj )

    def logToConsole( self ) :
        pass

class Powerup( GameObject ) :

    def __init__( self ) :
        super( Powerup, self ).__init__()

class PowerupDoubleShot( Powerup ) :

    def __init__( self ) :
        super( PowerupDoubleShot, self ).__init__()

class PowerupShield( Powerup ) :

    def __init__( self ) :
        super( PowerupShield, self ).__init__()

class PowerupBomb( Powerup ) :

    def __init__( self ) :
        super( PowerupBomb, self ).__init__()

class Hazard( GameObject ) :

    def __init__( self ) :
        super( Hazard, self ).__init__()

        self.m_damage = 10.0
        self.m_hitpoints = 5

class HazardAsteroid( Hazard ) :

    def __init__( self ) :
        super( HazardAsteroid, self ).__init__()

class HazardMissile( Hazard ) :

    def __init__( self ) :
        super( HazardMissile, self ).__init__()

class Factory( object ) :

    def __init__( self ) :
        super( Factory, self ).__init__()

    def create( self, params ) :
        raise NotImplementedError( 'ERROR> create method is virtual' )

class PowerupFactory( Factory ) :

    def __init__( self ) :
        super( PowerupFactory, self ).__init__()

    def create( self, params ) :
        pass

class HazardFactory( Factory ) :

    def __init__( self ) :
        super( HazardFactory, self ).__init__()

    def create( self, params ) :
        pass