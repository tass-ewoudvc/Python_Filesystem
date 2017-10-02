#!/usr/bin/env python

"""
Generates runnable Python skelton code to UnitTest a module
Accepts module name as parameter, writes code to file as second parameter

Tass PythonFundamentals course
Solution to: Refactor code generator
"""

import importlib  #pylint: disable=F0401
import inspect
import sys, os

if len(sys.argv) < 3:
    sys.exit("test_generator.py modulename outfile")

sys.path.append(os.getcwd())
mod_name = sys.argv[1]
mod_under_test = importlib.import_module(mod_name)
functions_in_module = inspect.getmembers(mod_under_test, inspect.isfunction)


string = '''#!/usr/bin/env python
"""Auto generated test module for: {0} """

import unittest
import {0} #pylint: disable=W0611

class Test{0}(unittest.TestCase):  #pylint: disable=R0904
    """
    Test class for {0}
    """'''.format(mod_name)

with open(sys.argv[2], "w") as fout:
    fout.write(string)

    for func, func_type in functions_in_module:
        string = '''    def test_{0}(self):"
                """ Tests{0}"""'
                self.assertTrue(False)

'''.format(func)
        fout.write(string)
        
    fout.write("unittest.main()\n")
