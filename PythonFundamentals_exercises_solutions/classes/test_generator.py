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
    sys.exit("Usage: test_generator.py modulename outfile")

sys.path.append(os.getcwd())
mod_name = sys.argv[1]
print(mod_name)
mod_under_test = importlib.import_module(mod_name)
functions_in_module = inspect.getmembers(mod_under_test, inspect.isfunction)
classes_in_module = inspect.getmembers(mod_under_test, inspect.isclass)

#-------------------------------------------------
string = '''#!/usr/bin/env python
"""Auto generated test module for: {0} """

#pylint: disable=R0904
#pylint: disable=W0611

import unittest
from {0} import *
'''.format(mod_name)
#-------------------------------------------------
class_string = '''
class Test{0}(unittest.TestCase): 
    """
    Test class for {0}
    """
'''
#-------------------------------------------------
method_string = '''    def test_{0}(self):
        """ Tests {0}"""
        self.assertTrue(False)

'''
#-------------------------------------------------
with open(sys.argv[2], "w") as fout:
    fout.write(string)

    # first the classes in module
    for class_name, class_type in classes_in_module:
        fout.write(class_string.format(class_name))
        funcs_in_class = inspect.getmembers(class_type, inspect.isfunction)
        for func, func_type in funcs_in_class:
            fout.write(method_string.format(func))


    # do the functions in module
    functions_in_module = list(functions_in_module)
    if len(functions_in_module):
        fout.write(class_string.format(mod_name))
        for func, func_type in functions_in_module:
            fout.write(method_string.format(func))
        
    fout.write("\nunittest.main()\n")
