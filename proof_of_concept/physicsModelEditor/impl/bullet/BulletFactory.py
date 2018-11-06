
from physicsModelEditor.core.IFactory import IFactory
from physicsModelEditor.impl.bullet.BulletJoint import BulletJoint

class BulletFactory( IFactory ) :

    def __init__( self ) :
        super( BulletFactory, self ).__init__()

    def _createDartJointObj( self, props ) :
        return object()
        
    def createJoint( self, props ) :
        # create an actual dart joint
        _dartJointObj = self._createDartJointObj( props )
        # wrappe it with the BulletJoint adapter
        _dartJoint = BulletJoint( _dartJointObj )

        return _dartJoint