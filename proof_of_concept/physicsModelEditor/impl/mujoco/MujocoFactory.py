
from physicsModelEditor.core.IFactory import IFactory
from physicsModelEditor.impl.mujoco.MujocoJoint import MujocoJoint

class MujocoFactory( IFactory ) :

    def __init__( self ) :
        super( MujocoFactory, self ).__init__()

    def _createDartJointObj( self, props ) :
        return object()
        
    def createJoint( self, props ) :
        # create an actual dart joint
        _dartJointObj = self._createDartJointObj( props )
        # wrappe it with the MujocoJoint adapter
        _dartJoint = MujocoJoint( _dartJointObj )

        return _dartJoint