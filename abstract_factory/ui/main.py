



class OSWidget( object ) :

    def __init__( self ) :
        super( OSWidget, self ).__init__()

    def show( self ) :
        raise NotImplementedError( 'ERROR> show method is pure virtual' )

# abstract widgets

class OSAbstractSlider( OSWidget ) :

    def __init__( self, props = {} ) :
        super( OSAbstractSlider, self ).__init__()

        # abstract properties
        self.m_currentValue = 0.0

    def setValue( self, value ) :
        self.m_currentValue = value

    def getValue( self ) :
        return self.m_currentValue

class OSAbstractLabel( OSWidget ) :

    def __init__( self, text ) :
        super( OSAbstractLabel, self )

        # abstract properties
        self.m_text = text

    def setText( self, text ) :
        self.m_text = text

    def getText( self ) :
        return self.m_text



# platform dependent implementations

class UIWindowsSlider( OSAbstractSlider ) :

    def __init__( self, props ) :
        super( UIWindowsSlider, self ).__init__( props )

        # some internal properties for windows
        self.m_windowsSldInternalValue = 0.0
        self.m_windowsSldInternalScale = 2.0

    def show( self ) :
        print( 'Showing ui-windows slider' )

class UILinuxSlider( OSAbstractSlider ) :

    def __init__( self, props ) :
        super( UILinuxSlider, self ).__init__( props )

        # some internal properties for linux
        self.m_linuxSldInternalScale = 1.0
        self.m_linuxSldInternalOffset = 0.5

    def show( self ) :
        print( 'Showing ui-linux slider' )


class UIMacSlider( OSAbstractSlider ) :

    def __init__( self, props ) :
        super( UIMacSlider, self ).__init__( props )

        # some internal properties for macos
        self.m_macosSldInternalOffset = 1.5
        self.m_macosSldInternalScale = 1.0
        self.m_macosSldInternalState = 'slider-simple'

    def show( self ) :
        print( 'Showing ui-macos slider' )





class UIWindowsLabel( OSAbstractLabel ) :

    def __init__( self, text ) :
        super( UIWindowsLabel, self ).__init__( text )

        # some internal properties for windows
        self.m_windowsLblInternalValue = 0.0
        self.m_windowsLblInternalScale = 2.0

    def show( self ) :
        print( 'Showing ui-windows label' )

class UILinuxLabel( OSAbstractLabel ) :

    def __init__( self, text ) :
        super( UILinuxLabel, self ).__init__( text )

        # some internal properties for linux
        self.m_linuxLblInternalScale = 1.0
        self.m_linuxLblInternalOffset = 0.5

    def show( self ) :
        print( 'Showing ui-linux label' )


class UIMacLabel( OSAbstractLabel ) :

    def __init__( self, text ) :
        super( UIMacLabel, self ).__init__( text )

        # some internal properties for macos
        self.m_macosLblInternalOffset = 1.0
        self.m_macosLblInternalScale = 1.0
        self.m_macosLblInternalState = 'label-simple'

    def show( self ) :
        print( 'Showing ui-macos label' )


# abstract factory

class OSWidgetFactory( object ) :

    def __init__( self ) :
        super( OSWidgetFactory, self ).__init__()

    def createSlider( self, props ) :
        raise NotImplementedError( 'ERROR> createSLider is pure virtual' )

    def createLabel( self, props ) :
        raise NotImplementedError( 'ERROR> createLabel is pure virtual' )


# platform specific factories

class WindowsWidgetFactory( OSWidgetFactory ) :

    def __init__( self ) :
        super( WindowsWidgetFactory, self ).__init__()

    def createSlider( self, props ) :
        return UIWindowsSlider( props )

    def createLabel( self, props ) :
        return UIWindowsLabel( props['text'] )

class LinuxWidgetFactory( OSWidgetFactory ) :

    def __init__( self ) :
        super( LinuxWidgetFactory, self ).__init__()

    def createSlider( self, props ) :
        return UILinuxSlider( props )

    def createLabel( self, props ) :
        return UILinuxLabel( props['text'] )

class MacWidgetFactory( OSWidgetFactory ) :

    def __init__( self ) :
        super( MacWidgetFactory, self ).__init__()

    def createSlider( self, props ) :
        return UIMacSlider( props )

    def createLabel( self, props ) :
        return UIMacLabel( props['text'] )


# abstract client

class OSApp( object ) :

    def __init__( self, uiFactory, layout = {} ) :
        super( OSApp, self ).__init__()

        # particular factory to create the widgets
        self.m_uiFactory = uiFactory

        # Defines the layout of the UI, namely ...
        # which widgets and how are they positioned
        self.m_layout = layout
        self.m_uiWidgets = {}

    def initialize( self ) :
        for _widgetId in self.m_layout :
            _widgetInfo = self.m_layout[ _widgetId ]
            _widgetType = _widgetInfo['type']
            if _widgetType == 'slider' :
                self.m_uiWidgets[_widgetId] = self.m_uiFactory.createSlider( _widgetInfo )
            elif _widgetType == 'label' :
                self.m_uiWidgets[_widgetId] = self.m_uiFactory.createLabel( _widgetInfo )



if __name__ == '__main__' :
    _windowsApp = OSApp( WindowsWidgetFactory(), {} )
    _linuxApp = OSApp( LinuxWidgetFactory(), {} )
    _macApp = OSApp( MacWidgetFactory(), {} )
