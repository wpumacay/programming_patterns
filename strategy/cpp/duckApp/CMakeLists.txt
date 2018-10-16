cmake_minimum_required( VERSION 3.0.0 )

project( duckApp )

set( CMAKE_CXX_STANDARD 11 )

add_executable( test_ducks
                duckApp.cpp
                test_ducks.cpp )