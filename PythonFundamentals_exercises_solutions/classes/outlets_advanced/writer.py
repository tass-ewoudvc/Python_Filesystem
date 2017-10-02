

'''
Module with helper class

Tass PythonFundamentals course
Solution to: Power outlets
'''

class MockWriter(object):
    '''
    Simple "Mock" (intelligente fake) class
    Could have used mock (framework), but havn't introduced it into course at this point

    Acts like a non generic Mock:
    Has the write method, but we needed to write this class, not really reusable ..

    It's generic in the way that it forwards data to another function.
    Set (for example) a lambda that checks the format of data as this function
    '''
    def __init__(self):
        self.checker_func = None

    def write(self, data):
        ''' "Mock" like method '''
        self.checker_func(data)
