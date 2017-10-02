#!/usr/bin/env python

'''
Test Module for AwesomeOutletsBank class

Tass PythonFundamentals course
Solution to: Power outlets
'''

#pylint: disable=C0301,W0401,R0904,W0611,W0614,R0903,R0904

import unittest
from awesome import *
from test_poweroutlet import * # will also run those tests ...

from writer import MockWriter

class TestAwesomeOutletsBank(unittest.TestCase):
    ''' Test class for AwesomeOutletBank '''

    def setUp(self):
        self.writer = MockWriter()  #
        self.bank = AwesomeOutletsBank(self.writer, 4)


    def test_constructor(self):
        ''' Tests the AwesomeOutletBank constructor '''
        self.assertRaises(AssertionError, AwesomeOutletsBank, None, 0)
        self.assertRaises(AssertionError, AwesomeOutletsBank, self.writer, 0)
        self.assertRaises(AssertionError, AwesomeOutletsBank, self.writer, 7)

        self.assertEqual(self.bank.writer, self.writer)
        self.assertEqual(len(self.bank.outlets), 4)

    def test_get_outlets(self):
        ''' Tests the get_outlets method '''
        self.assertEqual(4, len(self.bank.get_outlets()))

    def test_set_outlet_state(self):
        ''' Tests the set_outlet_state method '''
        # Assign a checker function to the MockWriter that checks if the correct data is being sent
        self.writer.checker_func = lambda x : self.assertEqual(x, "%1=0;")
        self.bank.set_outlet_state(1, PowerOff)

        self.writer.checker_func = lambda x : self.assertEqual(x, "%2=1;")
        self.bank.set_outlet_state(2, PowerOn)

        self.assertRaises(AssertionError, self.bank.set_outlet_state, 0, PowerOn)
        self.assertRaises(AssertionError, self.bank.set_outlet_state, 5, PowerOn)
        self.assertRaises(AssertionError, self.bank.set_outlet_state, 0, 3)


if __name__ == "__main__":
    unittest.main()   # pragma: no cover
