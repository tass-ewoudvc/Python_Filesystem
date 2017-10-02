
'''
Module for YouControls power bank control

Tass PythonFundamentals course
Solution to: Power outlets
'''
#pylint: disable=C0301

from poweroutlet import PowerOutletBank, PowerOutlet, PowerOn, PowerOff

class YouControlsBank(PowerOutletBank):
    '''
    Abstraction for AwesomeOutlet power outlet bank
    Requires an object to write to, like an open file or something
    Will be used like writer.write("string")
    '''
    def __init__(self, writer, num_outlets):
        assert num_outlets in (6, 12), "Use only 6 of 12"
        assert writer, "writer cannot be None"
        assert hasattr(writer, "write"), "writer needs to have a method write()"

        self.writer = writer
        outlets = []
        for i in range(num_outlets):
            outlets.append(PowerOutlet(self, i))
        self.outlets = tuple(outlets)

        self.states = 0 # Assume this is true at init

    def get_outlets(self):
        '''
        Returns a tuple of PowerOutlet objects in this bank
        '''
        return self.outlets

    def set_outlet_state(self, outlet_id, outlet_state):
        '''
        Sets outlet correstponding to outlet_id to state corresponding outlet_state
        '''
        assert(outlet_id in range(len(self.outlets)))
        assert(outlet_state in (PowerOn, PowerOff))

        if outlet_state is PowerOff:
            self.states &= ~(1 << outlet_id)
        else:
            self.states |= 1 << outlet_id

        self.writer.write("{states:0{width}b}\n".format(outlet_id, states = self.states, width = len(self.outlets)))

