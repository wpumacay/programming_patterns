
import time

# Resources we need to make a simpler API for ##############################################

class Turbine( object ) :

    MODE_LOW = 0
    MODE_MID = 1
    MODE_HIGH = 2

    def __init__( self ) :
        super( Turbine, self ).__init__()

        self.m_isOn = False
        self.m_mode = Turbine.MODE_LOW

    def on( self ) :
        self.m_isOn = True
        self.m_mode = Turbine.MODE_LOW
        print( 'Turbine ON' )

    def off( self ) :
        self.m_isOn = False
        self.m_mode = Turbine.MODE_LOW
        print( 'Turbine OFF' )

    def setMode( self, mode ) :
        if not self.m_isOn :
            print( 'WARNING> turbine should be on to set mode' )
        elif mode < Turbine.MODE_LOW or mode > Turbine.MODE_HIGH :
            print( 'WARNING> wrong mode requested to turbine' )
        else :
            self.m_mode = mode


class Boiler( object ) :

    def __init__( self ) :
        super( Boiler, self ).__init__()

        self.m_isOn = False
        self.m_minTargetTemperature = 100.0
        self.m_maxTargetTemperature = 300.0
        self.m_targetTemperature = self.m_minTargetTemperature

    def turnOn( self ) :
        self.m_isOn = True
        self.m_targetTemperature = self.m_minTargetTemperature
        print( 'Boiler ON' )

    def turnOff( self ) :
        self.m_isOn = False
        self.m_targetTemperature = self.m_minTargetTemperature
        print( 'Boiler OFF' )

    def setTargetTemperature( self, temperature ) :
        if ( temperature < self.m_minTargetTemperature or
             temperature > self.m_maxTargetTemperature ) :
             print( 'WARNING> Tried to set too low or too high target temperature' )
        else :
            self.m_targetTemperature = temperature

    def getTargetTemperature( self ) :
        return self.m_targetTemperature


# some resources not encapsulated in classes
def initializeTransformers() :
    print( 'Transformers initialized' )

def shutdownTransformers() :
    print( 'Shutting down transformers' )


# ##########################################################################################

# Common/Simple API ########################################################################

class ControlPanel( object ) :

    OPMODE_NORMAL = 0
    OPMODE_FULLCAPACITY = 1

    def __init__( self, turbine, boiler ) :
        super( ControlPanel, self ).__init__()

        self.m_turbine = turbine
        self.m_boiler = boiler

        self.m_isOn = False
        self.m_opMode = ControlPanel.OPMODE_NORMAL

    def startPlant( self ) :
        print( 'Starting plant' )

        initializeTransformers()
        self.m_turbine.on()
        self.m_boiler.turnOn()
        self.m_isOn = True

        self.setOperationMode( ControlPanel.OPMODE_NORMAL )

    def stopPlant( self ) :
        print ( 'Stopping plant' )

        self.m_isOn = False
        self.m_boiler.turnOff()
        self.m_turbine.off()
        shutdownTransformers()

    def setOperationMode( self, mode ) :
        if not self.m_isOn :
            print( 'WARNING> The plant should be started first' )
        elif mode == ControlPanel.OPMODE_NORMAL :
            self.m_opMode = mode
            self.m_turbine.setMode( Turbine.MODE_MID )
            self.m_boiler.setTargetTemperature( 150.0 )
            print( 'Set the opmode to NORMAL' )

        elif mode == ControlPanel.OPMODE_FULLCAPACITY :
            self.m_opMode = mode
            self.m_turbine.setMode( Turbine.MODE_HIGH )
            self.m_boiler.setTargetTemperature( 250.0 )
            print( 'Set the opmode to FULLCAPACITY' )

        else :
            print( 'WARNING> Tried to set wrong operation mode' )

# ##########################################################################################

# Client usage of the API ##################################################################

if __name__ == '__main__' :
    _turbine = Turbine()
    _boiler = Boiler()
    _controlPanel = ControlPanel( _turbine, _boiler )
    
    _controlPanel.startPlant()
    time.sleep( 2 )
    _controlPanel.setOperationMode( ControlPanel.OPMODE_FULLCAPACITY )
    time.sleep( 2 )
    _controlPanel.stopPlant()
    time.sleep( 2 )
    