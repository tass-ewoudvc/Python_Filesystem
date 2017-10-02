#!/usr/bin/env python

'''
Module containing "abstract base classes" to work with controllable power
outlets in an imaginary test framework

Tass PythonFundamentals course
Solution to: Power outlets
'''

PowerOn = 1
PowerOff = 0

#pylint: disable=R0903,R0904,C0301

class PowerOutletBank(object):
    '''
    "abstract base class" for any power outlet bank abstraction
    '''
    def get_outlets(self):
        '''
        Returns a tuple of PowerOutlet objects in this bank
        '''
        raise NotImplementedError()

    def set_outlet_state(self, outlet_id, outlet_state):
        '''
        Sets outlet correstponding to outlet_id to state
        corresponding outlet_state
        '''
        raise NotImplementedError()



class PowerOutlet(object):
    '''
    "base" for any power outlet abstraction
    Usable as a generic abstraction as is
    '''
    def __init__(self, bank, identifier):
        assert hasattr(bank, "set_outlet_state"), "bank object needs to have set_outlet_state(identifier, state)"
        self.bank = bank
        self.identifier = identifier

    def set_state(self, outlet_state):
        '''
        Sets the state of this outlet to the corresponding outlet_state
        '''
        self.bank.set_outlet_state(self.identifier, outlet_state)

