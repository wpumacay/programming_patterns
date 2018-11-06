
from physicsModelEditor.core.IPhysicsHelper import IPhysicsHelper
from physicsModelEditor.core.IRendererHelper import IRendererHelper

class IEditor( object ) :

    def __init__( self, physicsHelper, rendererHelper ) :
        super( IEditor, self ).__init__()

        self.m_physicsHelper  = physicsHelper
        self.m_rendererHelper = rendererHelper

    