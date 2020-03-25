#include "black_scholes.h"
#include <iostream>

void Ping()
{
    std::cout << "Lib is alive" << std::endl;
}

void BlackScholes_Foo(double* price_data, int data_size)
{
    for (int i = 0; i < data_size; ++i)
    {
        std::cout << price_data[i] << std::endl;
    }
}
