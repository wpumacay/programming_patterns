
import math, random
import matplotlib.pyplot as plt

from collections import deque

class IObserver( object ) :

    def __init__( self, observable ) :
        super( IObserver, self ).__init__()
        self.m_observable = observable

    def setObservable( self, observable ) :
        if self.m_observable is not None :
            self.m_observable.remove( self )
        self.m_observable = observable

    def onNotify( self ) :
        raise NotImplementedError()


class IObservable( object ) :

    def __init__( self ) :
        self.m_observers = []

    def add( self, observer ) :
        if observer not in self.m_observers :
            self.m_observers.append( observer )
    
    def remove( self, observer ) :
        if observer not in self.m_observers :
            return
        self.m_observers.remove( observer )

    def notify( self ) :
        for _observer in self.m_observers :
            _observer.onNotify()




class WeatherStation( IObservable ) :

    def __init__( self ) :
        super( WeatherStation, self ).__init__()

        self.m_temperature = 20.0
        self.m_pressure = 0.99
        self.m_humidity = 0.81
        self.m_forecast = 'rainy'
        self.m_time = 0.0

    def getState( self ) :
        _state = { 'temperature' : self.m_temperature,
                   'pressure' : self.m_pressure,
                   'humidity' : self.m_humidity,
                   'forecast' : self.m_forecast,
                   'time' : self.m_time }
        
        return _state

    """
    Call it to simulate the weather data
    """
    def simulation( self ) :
        self.m_time += 0.1
        self.m_temperature = 20.0 + 0.1 * math.sin( self.m_time ) + 0.2 * random.random()
        self.m_pressure = 0.99 + 0.25 * random.random()
        self.m_humidity = 0.81 + 0.1 * random.random()
        self.m_forecast = 'rainy' if ( int( self.m_time ) % 2 == 0 ) else 'sunny'

        self.notify()

class PlotDisplay( IObserver ) :

    def __init__( self, observable ) :
        super( PlotDisplay, self ).__init__( observable )

        # initialize matplotlib interactive mode
        plt.ion()
        # craete plotting resources
        # self.m_fig = plt.figure(1)
        # self.m_axs = self.m_fig.add_subplot( 1, 1, 1 )
        # ploting queue
        self.m_plotQueue = deque( [], maxlen = 20 )

    def onNotify( self ) :
        _stationState = self.m_observable.getState()
        self.m_plotQueue.append( ( _stationState['time'],
                                   _stationState['temperature'] ) )

    def plot( self ) :
        # self.m_axs.clear()
        # self.m_fig.clear()
        plt.cla()
        plt.clf()

        _data = list( self.m_plotQueue )
        _time = [ _entry[0] for _entry in _data ]
        _temperature = [ _entry[1] for _entry in _data ]
        plt.plot( _time, _data, 'b' )

class WeatherLogger( IObserver ) :

    def __init__( self, observable ) :
        super( WeatherLogger, self ).__init__( observable )
        # logging queue
        self.m_logQueue = deque( [], maxlen = 10 )

    def onNotify( self ) :
        _stationState = self.m_observable.getState()
        self.m_logQueue.append( ( _stationState['time'],
                                  _stationState['humidity'],
                                  _stationState['forecast'] ) )

    def logToConsole( self ) :
        print( 'Weather logs *************' )
        _data = list( self.m_logQueue )
        for _entry in _data :
            print( 'time: ', _entry[0] )
            print( 'humidity: ', _entry[1] )
            print( 'forecast: ', _entry[2] )
        
        print( '**************************' )


if __name__ == '__main__' :
    _station = WeatherStation()
    _plotter = PlotDisplay( _station )
    _logger = WeatherLogger( _station )

    _station.add( _plotter )
    _station.add( _logger )

    while True :
        _station.simulation()

        _plotter.plot()
        _logger.logToConsole()

        plt.pause( 0.1 )