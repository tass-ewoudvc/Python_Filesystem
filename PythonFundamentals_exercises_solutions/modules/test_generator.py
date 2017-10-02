#!/usr/bin/env python


"""
Generates runnable Python skelton code to UnitTest a module
Accepts module name as parameter, prints code to stdout

Tass PythonFundamentals course
Solution to: Python UnitTest Skeleton generator
"""

import importlib  #pylint: disable=F0401
import inspect
import sys

if len(sys.argv) < 2:
    sys.exit("I expect a module name as argument")

mod_name = sys.argv[1]
mod_under_test = importlib.import_module(mod_name)
# functions_in_module = (k for k, v in mod_under_test.__dict__.items()
#                        if isinstance(v, types.FunctionType))
functions_in_module = inspect.getmembers(mod_under_test, inspect.isfunction)


print '#!/usr/bin/env python'
print '"""Auto generated test module for:', mod_name, '"""'
print
print "import unittest"
print "import", mod_name,  "#pylint: disable=W0611"  #pylint: disable=E0012
print
print "class Test"+mod_name+"(unittest.TestCase):  #pylint: disable=R0904"   #pylint: disable=E0012
print '    """'
print '    Test class for', mod_name
print '    """'

for func, func_type in functions_in_module:
    print "    def test_"+func+"(self):"
    print '        """ Tests', func, '"""'
    print '        self.assertTrue(False)'
    print

print "unittest.main()"
