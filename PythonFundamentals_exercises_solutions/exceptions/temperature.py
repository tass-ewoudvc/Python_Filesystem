#!/usr/bin/env python

"""
Temperature conversion functions

Can be executed as a program

Tass PythonFundamentals course
Solution to: Temperature Conversion Module refactoring
"""

import argparse

_absolute_zero_c = 273.15
_absolute_zero_f = 459.67

_exception_message = "Temperature cannot be smaller than the absolute zero"

def c2k(temperature):
    """Convert Celsius to Kelvin"""
    assert(temperature >= -_absolute_zero_c)
    return temperature + _absolute_zero_c

def k2c(temperature):
    """Convert Kelvin to Celsius"""
    assert(temperature >= 0)
    return temperature - _absolute_zero_c

def c2f(temperature):
    """Convert Celsius to Fahrenheit"""
    assert(temperature >= -_absolute_zero_c)
    return (temperature * 9.0/5) + 32

def f2c(temperature):
    """Convert Fahrenheit to Celsius"""
    assert(temperature >= -_absolute_zero_f)
    return (temperature - 32.0) * 5/9

def f2k(temperature):
    """Convert Fahrenheit to Kelvin"""
    assert(temperature >= -_absolute_zero_f)
    return c2k(f2c(temperature))

def k2f(temperature):
    """Convert Kelvin to Fahrenheit"""
    assert(temperature >= 0)
    return c2f(k2c(temperature))



# The program
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--c2k", type=int, action="append",
                        help="Convert Celsius to Kelvin")
    parser.add_argument("--k2c", type=int, action="append",
                        help="Convert Kelvin to Celsius")
    parser.add_argument("--c2f", type=int, action="append",
                        help="Convert Celsius to Fahrenheit")
    parser.add_argument("--f2c", type=int, action="append",
                        help="Convert Fahrenheit to Celsius")
    parser.add_argument("--k2f", type=int, action="append",
                        help="Convert Kelvin to Fahrenheit")
    parser.add_argument("--f2k", type=int, action="append",
                        help="Convert Fahrenheit to Kelvin")

    args = parser.parse_args()

    if args.c2k:
        for val in args.c2k:
            print(val, "Celsius is", c2k(val), "Kelvin")

    if args.k2c:
        for val in args.k2c:
            print( val, "Kelvin is", k2c(val), "Celsius")

    if args.c2f:
        for val in args.c2f:
            print( val, "Celsius is", c2f(val), "Fahrenheit")

    if args.f2c:
        for val in args.f2c:
            print( val, "Fahrenheit is", f2c(val), "Celsius")

    if args.k2f:
        for val in args.k2f:
            print( val, "Kelvin is", k2f(val), "Fahrenheit")

    if args.f2k:
        for val in args.f2k:
            print( val, "Fahrenheit is", f2k(val), "Kelvin")
