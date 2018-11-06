
from physicsModelEditor.core.IFactory import IFactory
from physicsModelEditor.impl.dart.DartJoint import DartJoint

class DartFactory( IFactory ) :

    def __init__( self ) :
        super( DartFactory, self ).__init__()

    def _createDartJointObj( self, props ) :
        return object()
        
    def createJoint( self, props ) :
        # create an actual dart joint
        _dartJointObj = self._createDartJointObj( props )
        # wrappe it with the DartJoint adapter
        _dartJoint = DartJoint( _dartJointObj )

        return _dartJoint