#!/usr/bin/env python
"""Auto generated test module for: poweroutlet """

#pylint: disable=C0301,W0401,R0904,W0611,W0614,R0903,R0904

import unittest
from poweroutlet import *


class TestPowerOutletBank(unittest.TestCase):
    """
    Test class for PowerOutletBank
    Almost a moot unit test, we only assert that indeed the NotImplementedErrors are raised
    """
    bank = None

    def setUp(self):
        self.bank = PowerOutletBank()

    def test_get_outlets(self):
        '''Tests get_outlets method'''
        self.assertRaises(NotImplementedError, self.bank.get_outlets)


    def test_set_outlet_state(self):
        '''Tests set_outlet_state method'''
        self.assertRaises(NotImplementedError, self.bank.set_outlet_state, 0, PowerOn)


        

class BankMock(object):
    '''
    "Mock" (intelligent fake) class for PowerOutletBank

    To test a PowerOutlet in isolation (== without a real Bank),
    we need something that looks like a Bank from the outside,
    but where we can actually control what happens in the test.
    You don't want these tests to actually write to a serial port or socket now do you?

    Our implementation of the mock is a very simple one:
    * It just passes the data it recieves on to another function which should assert the correctness of the data
    
    There are Mocking frameworks designed just to do these things.
    Don't do this by manually in real life! Look into a framework
    But No Mocking framework was introduced at this point in the course, so we code it manually ...
    '''
    def __init__(self, checker_func):
        self.checker_func = checker_func

    def set_outlet_state(self, outlet_id, outlet_state):
        ''' Mock method, all Banks have it '''
        self.checker_func(outlet_id, outlet_state)



class TestPowerOutlet(unittest.TestCase):  #pylint: disable=R0904
    """
    Test class for PowerOutlet
    """
    outlet = None

    def setUp(self):
        self.outlet = PowerOutlet(PowerOutletBank(), 1)


    def test_constructor(self):
        ''' Tests constructor '''
        self.assertIsNotNone(self.outlet.bank)
        self.assertEqual(1, self.outlet.identifier)

    def test_set_state(self):
        '''Tests set_outlet_state method'''
        self.assertRaises(NotImplementedError, self.outlet.set_state, PowerOn)

        def helper(x, y):
            '''Helper for callback by BankMock'''
            self.assertEqual(x, 1)
            self.assertEqual(y, PowerOff)

        self.outlet.bank = BankMock(helper) # Replace the bank with a Mock one
        self.outlet.set_state(PowerOff)  # set_state will call set_outlet_state on the BankMock, which in turn will call our helper function




if __name__ == '__main__':  
    unittest.main()  # pragma: no cover
