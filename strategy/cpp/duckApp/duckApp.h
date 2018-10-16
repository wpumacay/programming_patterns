
#pragma once

#include <string>
#include <iostream>

namespace ducks
{


    class FlyBehaviour
    {
        public :

        FlyBehaviour() {}
        ~FlyBehaviour() {}

        virtual float run() = 0;
    };

    class FlyWithWings : public FlyBehaviour
    {
        public :

        FlyWithWings() : FlyBehaviour() {}
        ~FlyWithWings() {}

        float run() override;
    };

    class FlyWithBarrelRoll : public FlyBehaviour
    {
        public :

        FlyWithBarrelRoll() : FlyBehaviour() {}
        ~FlyWithBarrelRoll() {}

        float run() override;
    };

    class FlyNoWay : public FlyBehaviour
    {
        public :

        FlyNoWay() : FlyBehaviour() {}
        ~FlyNoWay() {}

        float run() override;
    };

    class QuackBehaviour
    {
        public :

        QuackBehaviour() {}
        ~QuackBehaviour() {}

        virtual void run() = 0;
    };

    class QuackSimple : public QuackBehaviour
    {
        public :

        QuackSimple() : QuackBehaviour() {}
        ~QuackSimple() {}

        void run() override;
    };

    class QuackLikePeppy : public QuackBehaviour
    {
        public :

        QuackLikePeppy() : QuackBehaviour() {}
        ~QuackLikePeppy() {}

        void run() override;
    };

    class QuackSqueak : public QuackBehaviour
    {
        public :

        QuackSqueak() : QuackBehaviour() {}
        ~QuackSqueak() {}

        void run() override;
    };

    class Duck
    {

        protected :

        std::string m_name;
        float m_height;

        FlyBehaviour* m_flyBehaviour;
        QuackBehaviour* m_quackBehaviour;

        public :

        Duck( const std::string& duckName );
        ~Duck();

        void fly();
        void quack();

        std::string name() { return m_name; }
        float height() { return m_height; }

    };


    class StarfoxDuck : public Duck
    {
        public :

        StarfoxDuck( const std::string& duckName );
        ~StarfoxDuck();
    };

    class SimpleDuck : public Duck
    {
        public :

        SimpleDuck( const std::string& duckName );
        ~SimpleDuck();
    };

}