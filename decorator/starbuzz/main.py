

class Beverage( object ) :

    def __init__( self ) :
        pass

    def description( self ) :
        raise NotImplementedError( "ERROR> description method is virtual" )

    def cost( self ) :
        raise NotImplementedError( "ERROR> cost method is virtual" )

###################################################
# Concrete beverages (like base cases in recursion)
###################################################

class Decaf( Beverage ) :

    def __init__( self ) :
        super( Decaf, self ).__init__()

    def description( self ) :
        return "Decaf"

    def cost( self ) :
        return 1.0

class Espresso( Beverage ) :

    def __init__( self ) :
        super( Espresso, self ).__init__()

    def description( self ) :
        return "Espresso"

    def cost( self ) :
        return 1.5

###################################################
# Decorators definitions
###################################################

class AddonDecorator( Beverage ) :

    def __init__( self, wrappedObj ) :
        super( AddonDecorator, self ).__init__()

        self.m_wrappedObj = wrappedObj


class Caramel( AddonDecorator ) :

    def __init__( self, wrappedObj ) :
        super( Caramel, self ).__init__( wrappedObj )

    def description( self ) :
        return ( self.m_wrappedObj.description() + ' with Caramel' )

    def cost( self ) :
        return 0.2 + self.m_wrappedObj.cost()

class Soy( AddonDecorator ) :

    def __init__( self, wrappedObj ) :
        super( Soy, self ).__init__( wrappedObj )

    def description( self ) :
        return ( self.m_wrappedObj.description() + ' with Soy' )

    def cost( self ) :
        return 0.15 + self.m_wrappedObj.cost()



if __name__ == '__main__' :
    # create some fancy beverages
    _decaf_caramel = Caramel( Decaf() )
    _decaf_soy = Soy( Decaf() )
    _espresso_caramel = Caramel( Espresso() )
    _espresso_soy = Soy( Espresso() )
    _espresso_caramel_soy_caramel_soy = Caramel( Soy( Caramel( Soy( Espresso() ) ) ) )

    _fancy_beverages = [ _decaf_caramel, _decaf_soy, 
                         _espresso_caramel, _espresso_soy,
                         _espresso_caramel_soy_caramel_soy ]

    for _beverage in _fancy_beverages :
        print( 'Description: ', _beverage.description() )
        print( 'Cost: ', _beverage.cost() )