

class IRendererHelper( object ) :

    def __init__( self ) :
        super( IRendererHelper, self ).__init__()

    def renderUI( self ) :
        pass

    def rotateCamera( self ) :
        pass

    def pickElement( self ) :
        pass

    def moveElement( self, name ) :
        pass

    def rotateElement( self, name ) :
        pass

    def scaleElement( self, name ) :
        pass

    def createElement( self, name, props ) :
        pass
