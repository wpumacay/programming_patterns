



class ShaderManager( object ) :

    _INSTANCE = None

    @staticmethod
    def getInstance() :
        if ShaderManager._INSTANCE is None :
            ShaderManager._INSTANCE = ShaderManager()
        return ShaderManager._INSTANCE

    def __init__( self ) :
        super( ShaderManager, self ).__init__()

        self.m_shaders = {}

    def loadShader( self, filename, shaderId ) :
        print( 'INFO> creating shader from file: ', filename )

    def getShader( self, shaderId ) :
        if shaderId not in self.m_shaders :
            return None
        return self.m_shaders[ shaderId ]
        

class AssetsManager( object ) :

    _INSTANCE = None

    @staticmethod
    def getInstance() :
        if AssetsManager._INSTANCE is None :
            AssetsManager._INSTANCE = AssetsManager()
        return AssetsManager._INSTANCE

    def __init__( self ) :
        super( AssetsManager, self ).__init__()

        self.m_textures = {}

    def loadTexture( self, filename, textureId ) :
        print( 'INFO> loading texture from file: ', filename )

    def getTexture( self, textureId ) :
        if textureId not in self.m_textures :
            return None
        return self.m_textures[ textureId ]


def loadResources( shaders, textures ) :
    # load shaders
    _shaderManager = ShaderManager.getInstance()

    for _shader in shaders :
        _shaderId = _shader['id']
        _shaderFilename = _shader['filename']
        _shaderManager.loadShader( _shaderFilename, _shaderId )

    # load textures
    _assetsManager = AssetsManager.getInstance()

    for _texture in textures :
        _textureId = _texture['id']
        _textureFilename = _texture['filename']
        _assetsManager.loadTexture( _textureFilename, _textureId )

def getShader( shaderId ) :
    _shaderManager = ShaderManager.getInstance()
    return _shaderManager.getShader( shaderId )

def getTexture( textureId ) :
    _assetsManager = AssetsManager.getInstance()
    return _assetsManager.getTexture( textureId )