
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import requests, io
import threading
import time

class IImage( object ) :

    def __init__( self ) :
        super( IImage, self ).__init__()

    def buffer( self ) :
        raise NotImplementedError( 'ERROR> buffer is pure virtual' )

    def ready( self ) :
        raise NotImplementedError( 'ERROR> ready is pure virtual' )

class IconImage( IImage ) :

    def __init__( self, uri ) :
        super( IconImage, self ).__init__()

        self.m_uri = uri
        self.m_imgBuffer = None
        self.m_loaded = False

        self.m_lock = threading.Lock()
        self.m_loaderWorker = None

        self._loadImage()

    def _loadImage( self ) :
        print( 'Started loading resource' )
        self.m_loaderWorker = threading.Thread( target = self._loaderWorkerFcn )
        self.m_loaderWorker.start()

    def _loaderWorkerFcn( self ) :
        time.sleep( 5 )
        _response = requests.get( self.m_uri )
        self.m_imgBuffer = mpimg.imread( io.BytesIO( _response.content ) )
        
        self.m_lock.acquire( True )
        print( 'Finished loading resource' )
        self.m_loaded = True
        self.m_lock.release()

    def ready( self ) :
        return self.m_loaded

    def buffer( self ) :
        return self.m_imgBuffer

class ProxyImage( IImage ) :

    def __init__( self, uri ) :
        super( ProxyImage, self ).__init__()

        self.m_imgRef = IconImage( uri )

    def buffer( self ) :
        if self.m_imgRef.ready() :
            return self.m_imgRef.buffer()
        else :
            return 255.0 * np.random.random( ( 100, 100 ) )

    def ready( self ) :
        return True





if __name__ == '__main__' :
    
    _img = ProxyImage( 'https://raw.githubusercontent.com/wpumacay/dm_control/master/dm_control/glviz/_imgs/img_controlsuite_viz_implementation_overview.png' )

    plt.ion()
    while True :
        plt.clf()
        plt.cla()
        plt.imshow( _img.buffer() )
        plt.pause( 0.1 )