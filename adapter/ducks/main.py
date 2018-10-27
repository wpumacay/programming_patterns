

# TARGET (What our client wants to use)

class Duck( object ) :

    def __init__( self, name ) :
        super( Duck, self ).__init__()

        self.m_name = name

    def name( self ) :
        return self.m_name

    def quack( self ) :
        raise NotImplementedError( 'ERROR> quack is pure virtual' )

    def fly( self ) :
        return NotImplementedError( 'ERROR> fly is pure virtual' )

# Some example of a Target that it uses

class CartoonDuck( Duck ) :

    def __init__( self, name ) :
        super( CartoonDuck, self ).__init__( name )

    def quack( self ) :
        print( 'CQuack: ', self.m_name )

    def fly( self ) :
        print( 'CFly: ', self.m_name )

# A different functionality/target which is not ...
# compatitble with the client's target

class Turkey( object ) :

    def __init__( self, name ) :
        super( Turkey, self ).__init__()

        self.m_name = name

    def name( self ) :
        return self.m_name

    def gobble( self ) :
        print( 'Turkey-%s: gobble, gobble, gobble' % ( self.m_name ) )
    
    def fly( self ) :
        print( 'Turkey-%s: flying!' % ( self.m_name ) )

# An adapter to our target, that wraps the non-compatible target

class TurkeyToDuckAdapter( Duck ) :

    def __init__( self, turkey ) :
        super( TurkeyToDuckAdapter, self ).__init__( turkey.name() )
        
        self.m_turkeyRef = turkey

    def quack( self ) :
        self.m_turkeyRef.gobble()

    def fly( self ) :
        for _ in range( 5 ) :
            self.m_turkeyRef.fly()

# A client of the target functionality

class DuckWorld( object ) :

    def __init__( self ) :
        super( DuckWorld, self ).__init__()

        self.m_ducks = []

    def addDuck( self, duck ) :
        self.m_ducks.append( duck )
    
    def party( self ) :
        for _duck in self.m_ducks :
            _duck.fly()
            _duck.quack()


if __name__ == '__main__' :

    _duckWorld = DuckWorld()
    _duckWorld.addDuck( CartoonDuck( 'daffy' ) )
    _duckWorld.addDuck( CartoonDuck( 'lucas' ) )
    _duckWorld.addDuck( TurkeyToDuckAdapter( Turkey( 'turkling' ) ) )

    _duckWorld.party()