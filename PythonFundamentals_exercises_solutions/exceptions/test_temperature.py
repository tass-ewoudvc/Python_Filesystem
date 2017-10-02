#!/usr/bin/env python

"""
Test program for temperature.py

Tass PythonFundamentals course
Solution to: Temperature Conversion Module refactoring
"""

import unittest
import temperature


class TestTemperature(unittest.TestCase):  #pylint: disable=R0904
    """
    Test class for Matrix Transposition
    """
    def test_c2k(self):
        """ Tests Celsius to Kelvin conversion """
        self.assertEqual(273.15, temperature.c2k(0))
        self.assertEqual(0, temperature.c2k(-273.15))
        self.assertEqual(373.15, temperature.c2k(100))
        self.assertRaises(AssertionError, temperature.c2k, -274)

    def test_k2c(self):
        """ Tests Kelvin to Celsius conversion """
        self.assertEqual(0, temperature.k2c(273.15))
        self.assertEqual(-273.15, temperature.k2c(0))
        self.assertEqual(100, temperature.k2c(373.15))
        self.assertRaises(AssertionError, temperature.k2c, -1)

    def test_c2f(self):
        """ Tests Celsius to Fahrenheit conversion"""
        self.assertEqual(212, temperature.c2f(100))
        self.assertEqual(122, temperature.c2f(50))
        self.assertEqual(32, temperature.c2f(0))
        self.assertRaises(AssertionError, temperature.c2f, -274)

    def test_f2c(self):
        """ Tests Fahrenheit to Celsius conversion"""
        self.assertEqual(10, temperature.f2c(50))
        self.assertEqual(66, temperature.f2c(150.8))
        self.assertRaises(AssertionError, temperature.f2c, -460)

    def test_f2k(self):
        """ Tests Fahrenheit to Kelvin """
        self.assertAlmostEqual(310.928, temperature.f2k(100), places=3)
        self.assertEqual(150, temperature.f2k(-189.67))
        self.assertRaises(AssertionError, temperature.f2k, -460)

    def test_k2f(self):
        """ Tests Kelvin to Fahrenheit """
        self.assertAlmostEqual(-459.67, temperature.k2f(0), places=3)
        self.assertEqual(-189.67, temperature.k2f(150))
        self.assertRaises(AssertionError, temperature.k2f, -1)


unittest.main()

