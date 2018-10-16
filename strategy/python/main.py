
from duckApp import StarFoxDuck, SimpleDuck

_sfoxDuck = StarFoxDuck()
_simpleDuck = SimpleDuck()

_sfoxDuck.fly()
_simpleDuck.fly()

if _sfoxDuck.height() > _simpleDuck.height() :
    print( 'sfox duck flies higher' )

_sfoxDuck.quack()
_simpleDuck.quack()