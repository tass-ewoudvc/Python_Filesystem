#!/usr/bin/env python
'''
Module containing PowerOutlet class, for use in testcases

Tass PythonFundamentals course
Solution to: Power outlets (basic)
'''

PowerOn = 1
PowerOff = 0

#pylint: disable=R0903,R0904,C0301



class PowerOutlet(object):
    '''
    PowerOutlet class implementing the protocol of AwesomeOutlets
    Create a bunch of these classes in setup code, and pass an instance along
    to the actual tests of the device you're powercycling.
    Thus separatig the test from it's hardware configuration.

    identifier: a number (starting with 1) used by the protocol
    communication: a class that has a write method, for sending data
    '''
    def __init__(self, identifier, communication):
        self.communication = communication
        self.identifier = identifier

    def set_state(self, outlet_state):
        '''
        Sets the state of this outlet to the corresponding outlet_state

        outlet_state: values of PowerOn or PowerOff (see symbols global in this module)
        '''
        self.communication.write("%{}={};".format(self.identifier, outlet_state))

