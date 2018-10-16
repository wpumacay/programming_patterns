
#include "duckApp.h"


int main()
{

    ducks::Duck* _sfoxDuck = new ducks::StarfoxDuck( "Peppy Duck" );
    ducks::Duck* _simpleDuck = new ducks::SimpleDuck( "Daffy Duck" );

    _sfoxDuck->fly();
    _simpleDuck->fly();

    if ( _sfoxDuck->height() > _simpleDuck->height() )
    {
        std::cout << "sfox duck flies higher" << std::endl;
    }

    _sfoxDuck->quack();
    _simpleDuck->quack();

    delete _sfoxDuck;
    delete _simpleDuck;

    return 0;
}