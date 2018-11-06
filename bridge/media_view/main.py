


# some external functionality we have to adapt to

class Artist( object ) :

    def __init__( self ) :
        super( Artist, self ).__init__()

        self.m_bio = None
        self.m_photo = None
        self.m_name = None

    def bio( self ) :
        return self.m_bio

    def photo( self ) :
        return self.m_photo

    def name( self ) :
        return self.m_name

class Book( object ) :

    def __init__( self ) :
        super( Book, self ).__init__()

        self.m_title = None
        self.m_summary = None
        self.m_coverPhoto = None

    def title( self ) :
        return self.m_title
    
    def summary( self ) :
        return self.m_summary

    def coverPhoto( self ) :
        return self.m_coverPhoto

# our media resources (concretions/implementation)

class AbstractMediaResource( object ) :

    def __init__( self ) :
        super( AbstractMediaResource, self ).__init__()

    def title( self ) :
        raise NotImplementedError( 'ERROR> title is pure virtual' )

    def description( self ) :
        raise NotImplementedError( 'ERROR> description is pure virtual' )

    def image( self ) :
        raise NotImplementedError( 'ERROR> image is pure virtual' )

class ArtistResource( AbstractMediaResource ) :

    def __init__( self, artist ) :
        super( ArtistResource, self ).__init__()

        self.m_artist = artist

    def title( self ) :
        return self.m_artist.name()

    def description( self )  :
        return self.m_artist.bio()

    def image( self ) :
        return self.m_artist.photo()

class BookResource( AbstractMediaResource ) :

    def __init__( self, book ) :
        super( BookResource, self ).__init__()

        self.m_book = book

    def title( self ) :
        return self.m_book.title()

    def description( self ) :
        return self.m_book.summary()

    def image( self ) :
        return self.m_book.coverPhoto()

# our views ("abstractions")

class AbstractView( object ) :

    def __init__( self, mediaResource ) :
        super( AbstractView, self ).__init__()

        self.m_mediaResource = mediaResource

    def show( self ) :
        raise NotImplementedError( 'ERROR> show is pure virtual' )

    # ... some other methods

class LongView( AbstractView ) :

    def __init__( self, mediaResource ) :
        super( LongView, self ).__init__( mediaResource )

    def show( self ) :
        print( 'title: ', self.m_mediaResource.title() )
        print( 'description: ', self.m_mediaResource.description() )
        print( 'image: ', self.m_mediaResource.image() )

class ShortView( AbstractView ) :

    def __init__( self, mediaResource ) :
        super( ShortView, self ).__init__( mediaResource )

    def show( self ) :
        print( 'title: ', self.m_mediaResource.title() )
        print( 'image: ', self.m_mediaResource.image() )