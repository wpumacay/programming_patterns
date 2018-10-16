
#include "duckApp.h"


namespace ducks
{

    float FlyWithWings::run()
    {
        return 2.0f;
    }

    float FlyWithBarrelRoll::run()
    {
        return 10.0f;
    }

    float FlyNoWay::run()
    {
        return 0.0f;
    }


    void QuackSimple::run()
    {
        std::cout << "Quack!!!, I am a duck" << std::endl;
    }

    void QuackLikePeppy::run()
    {
        std::cout << "DO A BARREL ROLL!!!" << std::endl;
    }

    void QuackSqueak::run()
    {
        std::cout << "Squeak, a plastic sound" << std::endl;
    }


    Duck::Duck( const std::string& duckName )
    {
        m_name = duckName;
        m_height = 0.0f;

        m_flyBehaviour = NULL;
        m_quackBehaviour = NULL;
    }

    Duck::~Duck()
    {
        std::cout << "deleting duck" << std::endl;

        if ( m_flyBehaviour != NULL )
        {
            delete m_flyBehaviour;
            m_flyBehaviour = NULL;
        }

        if ( m_quackBehaviour != NULL )
        {
            delete m_quackBehaviour;
            m_quackBehaviour = NULL;
        }
    }

    void Duck::fly()
    {
        if ( m_flyBehaviour != NULL )
        {
            m_height += m_flyBehaviour->run();
        }
    }

    void Duck::quack()
    {
        if ( m_quackBehaviour != NULL )
        {
            m_quackBehaviour->run();
        }
    }


    StarfoxDuck::StarfoxDuck( const std::string& duckName )
        : Duck( duckName )
    {
        m_flyBehaviour = new FlyWithBarrelRoll();
        m_quackBehaviour = new QuackLikePeppy();
    }

    StarfoxDuck::~StarfoxDuck()
    {

    }


    SimpleDuck::SimpleDuck( const std::string& duckName )
        : Duck( duckName )
    {
        m_flyBehaviour = new FlyWithWings();
        m_quackBehaviour = new QuackSimple();
    }

    SimpleDuck::~SimpleDuck()
    {
        
    }
}