

# Commands here are single/static, as they are created once and used ...
# always. If need to acommodate for varying parameters for a given command then ...
# the command should be created at request with the given info


# resources to handle in the world (RECEIVERS)

class Light( object ) :

    def __init__( self ) :
        super( Light, self ).__init__()

        self.m_isOn = False

    def turnOn( self ) :
        self.m_isOn = True

    def turnOff( self ) :
        self.m_isOn = False

    def isOn( self ) :
        return self.m_isOn

class ConfigurableLight( object ) :

    def __init__( self ) :
        super( ConfigurableLight, self ).__init__()

        self.m_intensity = 0.0
        self.m_minIntensity = 1.0
        self.m_maxIntensity = 10.0

        self.m_isOn = False

    def turnOn( self ) :
        self.m_isOn = True
        self.m_intensity = self.m_minIntensity

    def turnOff( self ) :
        self.m_isOn = False
        self.m_intensity = 0.0

    def isOn( self ) :
        return self.m_isOn

    def setIntensity( self, intensity ) :
        self.m_intensity = intensity
        self.m_intensity = self.m_maxIntensity if ( intensity > self.m_maxIntensity ) else intensity
        self.m_intensity = self.m_minIntensity if ( intensity < self.m_minIntensity ) else intensity

    def getIntensity( self ) :
        return self.m_intensity

    def minIntensity( self ) :
        return self.m_minIntensity

    def maxIntensity( self ) :
        return self.m_maxIntensity

# The commands to handle the devices

class Command( object ) :

    def __init__( self ) :
        super( Command, self ).__init__()

    def execute( self ) :
        raise NotImplementedError( 'ERROR> execute method is pure virtual' )

    def unexecute( self ) :
        raise NotImplementedError( 'ERROR> unexecute method is pure virtual' )

class LightOnCommand( Command ) :

    def __init__( self, light ):
        super( LightOnCommand, self ).__init__()

        self.m_light = light

    def execute( self ) :
        self.m_light.turnOn()

    def unexecute( self ) :
        self.m_light.turnOff()

class LightOffCommand( Command ) :

    def __init__( self, light ) :
        super( LightOffCommand, self ).__init__()

        self.m_light = light

    def execute( self ) :
        self.m_light.turnOff()

    def unexecute( self ) :
        self.m_light.turnOn()

class ConfigurableLightUpCommand( Command ) :

    def __init__( self, configurableLight ) :
        super( ConfigurableLightUpCommand, self ).__init__()

        self.m_configurableLight = configurableLight

    def execute( self ) :
        if not self.m_configurableLight.isOn() :
            self.m_configurableLight.turnOn()
            return

        _currentIntensity = self.m_configurableLight.getIntensity()
        self.m_configurableLight.setIntensity( _currentIntensity + 0.5 )

    def unexecute( self ) :
        if not self.m_configurableLight.isOn() :
            return

        _currentIntensity = self.m_configurableLight.getIntensity()
        if _currentIntensity <= self.m_configurableLight.minIntensity() :
            self.m_configurableLight.turnOff()
        else :
            self.m_configurableLight.setIntensity( _currentIntensity - 0.5 )

class ConfigurableLightDownCommand( Command ) :

    def __init__( self, configurableLight ) :
        super( ConfigurableLightDownCommand, self ).__init__()

        self.m_configurableLight = configurableLight

    def execute( self ) :
        if not self.m_configurableLight.isOn() :
            return

        _currentIntensity = self.m_configurableLight.getIntensity()
        if _currentIntensity >= self.m_configurableLight.minIntensity() :
            self.m_configurableLight.setIntensity( _currentIntensity - 0.5 )
        else :
            self.m_configurableLight.turnOff()

    def unexecute( self ) :
        if not self.m_configurableLight.isOn() :
            self.m_configurableLight.turnOn()
            return
        
        _currentIntensity = self.m_configurableLight.getIntensity()
        self.m_configurableLight.setIntensity( _currentIntensity + 0.5 )


# the remote control itself (INVOKER)


class RemoteControl( object ) :

    def __init__( self, 
                  slot1CommandOn, slot1CommandOff,
                  slot2CommandOn, slot2CommandOff ) :
        super( RemoteControl, self ).__init__()
        
        self.m_slot1CommandOn = slot1CommandOn
        self.m_slot1CommandOff = slot1CommandOff
        self.m_slot2CommandOn = slot2CommandOn
        self.m_slot2CommandOff = slot2CommandOff

    def clickSlot1On( self ) :
        self.m_slot1CommandOn.execute()

    def clickSlot1Off( self ) :
        self.m_slot1CommandOff.execute()

    def clickSlot2On( self ) :
        self.m_slot2CommandOn.execute()

    def clickSlot2Off( self ) :
        self.m_slot2CommandOff.execute()