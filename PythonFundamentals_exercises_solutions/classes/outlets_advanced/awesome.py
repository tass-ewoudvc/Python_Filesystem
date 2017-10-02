
'''
Module for AwesomeOutlets power bank control

Tass PythonFundamentals course
Solution to: Power outlets
'''
from poweroutlet import PowerOutletBank, PowerOutlet, PowerOn, PowerOff

class AwesomeOutletsBank(PowerOutletBank):
    '''
    Abstraction for AwesomeOutlet power outlet bank
    Requires an object to write to, like an open file or something
    Will be used like writer.write("string")
    '''
    def __init__(self, writer, num_outlets):
        assert num_outlets in (4, 8, 16), "Use only 4 ,8 or 16"
        assert writer, "writer cannot be None"
        assert hasattr(writer, "write"), "writer needs to have a method write()"

        self.writer = writer
        outlets = []
        for i in range(1, num_outlets+1):
            outlets.append(PowerOutlet(self, i))
        self.outlets = tuple(outlets)

    def get_outlets(self):
        '''
        Returns a tuple of PowerOutlet objects in this bank
        '''
        return self.outlets

    def set_outlet_state(self, outlet_id, outlet_state):
        '''
        Sets outlet correstponding to outlet_id to state
        corresponding outlet_state
        '''
        assert(outlet_id in range (1, len(self.outlets)+1))
        assert(outlet_state in (PowerOn, PowerOff))
        self.writer.write("%{0:d}={1:d};".format(outlet_id, outlet_state))

