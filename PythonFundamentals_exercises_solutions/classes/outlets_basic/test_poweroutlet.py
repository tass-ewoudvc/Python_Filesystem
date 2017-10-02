#!/usr/bin/env python
'''
Module containing test code for the  PowerOutlet class

Tass PythonFundamentals course
Solution to: Power outlets (basic)
'''

import unittest
import poweroutlet


class MockCommunication:
    '''
    A Mock (intelligent fake) communication class.
    This will help us assert some things in the tests

    There are frameworks that are specialized in Mocking!
    Look into these ....
    Don't do this by hand in anything but the simplest cases!
    '''
    def __init__(self):
        self.data = []

    def write(self, writedata):
        '''
        A Mock write function, that only stores what is sent
        '''
        self.data.append(writedata)


class TestPowerOutlet(unittest.TestCase):
    def setUp(self):
        '''
        Setup method for test class
        (see pydoc of unittest)
        '''
        self.communication = MockCommunication();
        self.outlet = poweroutlet.PowerOutlet(5, self.communication)
    
    def test_set_state_on(self):
        # do the actual action
        self.outlet.set_state(poweroutlet.PowerOn);

        # Assert that the Mock has received the correct data
        self.assertEqual(len(self.communication.data), 1)
        self.assertEqual(self.communication.data[0], "%5=1;")


    def test_set_state_off(self):
        # do the actual action
        self.outlet.set_state(poweroutlet.PowerOff);

        # Assert that the Mock has received the correct data
        self.assertEqual(len(self.communication.data), 1)
        self.assertEqual(self.communication.data[0], "%5=0;")       


unittest.main()
    
