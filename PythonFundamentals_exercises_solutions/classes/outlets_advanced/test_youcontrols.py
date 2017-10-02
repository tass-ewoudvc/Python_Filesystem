#!/usr/bin/env python

'''
Test Module for YouControlsBank class

Tass PythonFundamentals course
Solution to: Power outlets
'''

#pylint: disable=C0301,W0401,R0904,W0611,W0614,R0903,R0904

import unittest
from youcontrols import *
from test_poweroutlet import * # will also run those tests ...

from writer import MockWriter


class TestYouControlsBank(unittest.TestCase):
    ''' Test class for AwesomeOutletBank '''

    def setUp(self):
        self.writer = MockWriter()
        self.bank = YouControlsBank(self.writer, 6)
        self.bigbank = YouControlsBank(self.writer, 12)


    def test_constructor(self):
        ''' Tests the AwesomeOutletBank constructor '''

        # Try creating YouControlsBank instances with boguous data and assert that AssertionError is thrown ;-)
        self.assertRaises(AssertionError, YouControlsBank, None, 0)
        self.assertRaises(AssertionError, YouControlsBank, self.writer, 0)
        self.assertRaises(AssertionError, YouControlsBank, self.writer, 7)
 
        # Try creating YouControlsBank instances with correct data and see if indeed the correct number of outlets are created
        self.assertEqual(self.bank.writer, self.writer)
        self.assertEqual(len(self.bank.outlets), 6)

        self.assertEqual(self.bigbank.writer, self.writer)
        self.assertEqual(len(self.bigbank.outlets), 12)


    def test_get_outlets(self):
        ''' Tests the get_outlets method '''
        self.assertEqual(6, len(self.bank.get_outlets()))
        self.assertEqual(12, len(self.bigbank.get_outlets()))

        
    def test_set_outlet_state(self):
        ''' Tests the set_outlet_state method '''
        self.writer.checker_func = lambda x : self.assertEqual(x, "000000\n")
        self.bank.set_outlet_state(0, PowerOff)

        self.writer.checker_func = lambda x : self.assertEqual(x, "000100\n")
        self.bank.set_outlet_state(2, PowerOn)

        self.writer.checker_func = lambda x : self.assertEqual(x, "000101\n")
        self.bank.set_outlet_state(0, PowerOn)

        self.writer.checker_func = lambda x : self.assertEqual(x, "000100\n")
        self.bank.set_outlet_state(0, PowerOff)

        self.assertRaises(AssertionError, self.bank.set_outlet_state, 6, PowerOn)
        self.assertRaises(AssertionError, self.bank.set_outlet_state, 0, 3)

        self.writer.checker_func = lambda x : self.assertEqual(x, "000000000000\n")
        self.bigbank.set_outlet_state(0, PowerOff)

        self.writer.checker_func = lambda x : self.assertEqual(x, "100000000000\n")
        self.bigbank.set_outlet_state(11, PowerOn)

        self.assertRaises(AssertionError, self.bigbank.set_outlet_state, 12, PowerOn)



if __name__ == "__main__":
    unittest.main()
