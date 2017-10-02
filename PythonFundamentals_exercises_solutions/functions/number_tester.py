#!/usr/bin/env python

"""
Tass PythonFundamentals Course
Solution to: "Prime, Armstrong and Perfect number tester"
"""

import unittest

def is_armstrong(number):
    """ Tests if a number is an armstrong number """
    sum_of_digits = 0
    number_string = str(number)
    power = len(number_string)
    for char in number_string:
        sum_of_digits += int(char) ** power
    return sum_of_digits == number
    

def is_prime(number):
    """ Tests if a number is a prime """
    prime = True
    for divisor in range(2, number-1):
        if number % divisor == 0:
            prime = False
            break
    return prime


def is_perfect(number):
    """ Tests if a number is a perfect number """
    sum_of_divisors = 0
    for divisor in range(1, number//2+1):
        if number % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors == number



class TestAll(unittest.TestCase):
    """
    Test class for all 3 methods
    """
    def test_is_prime(self):
        """ Tests the is_prime function """
        primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        for number in range(2, 30):
            prime = is_prime(number)
            if number in primes:
                self.assertTrue(prime)
            else:
                self.assertFalse(prime)

    def test_is_armstrong(self):
        """ Test the is_armstrong function """
        for number in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153,
                       370, 371, 407, 1634, 8208, 9474):
            self.assertTrue(is_armstrong(number))

        for number in range(10, 152):
            self.assertFalse(is_armstrong(number))

    def test_is_perfect(self):
        """ Test the is_perfect function """
        perfects = (6, 28, 496, 8128)
        for number in perfects:
            self.assertTrue(is_perfect(number))

        for number in range(1, 40):
            if number not in perfects:
                self.assertFalse(is_perfect(number))

unittest.main()
