#ifndef BLACK_SCHOLES_H
#define BLACK_SCHOLES_H

#define DLLEXPORT __declspec(dllexport)

extern "C"
{
    void DLLEXPORT BlackScholes_Foo(double* price_data, int data_size);
}

#endif // BLACK_SCHOLES_H
