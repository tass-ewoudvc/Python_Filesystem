#!/usr/bin/env python

"""
Generates runnable C skeleton code to UnitTest a module using Check

Can also run as a program, with arguments being the function names

Tass PythonFundamentals course
Solution to: Python UnitTest Skeleton generator
"""

import sys

def generate_check(module, functions):
    """Generates skeleton C code for a Check UnitTest"""
    print "//Automatically generated code to Check module ", module
    print
    print "#include <stdlib.h>"
    print "#include <check.h>"
    print '#include "'+module+'.h"'
    print "//------------------------------------------------------------"

    for func in functions:
        print "START_TEST (test_"+func+")"
        print "{"
        print "    ck_assert(0);"
        print "}"
        print "END_TEST"
        print "//------------------------------------------------------------"

    print "Suite*", module+"_suite()"
    print "{"
    print '    Suite* s = suite_create("'+module+'");'
    print '    TCase* core = tcase_create("Core");'
    for func in functions:
        print '    tcase_add_test(core, test_'+func+');'
    print "    suite_add_tcase(s, core);"
    print "    return s;"
    print "}"
    print "//------------------------------------------------------------"

    print "int main()"
    print "{"
    print "    int number_failed;"
    print "    Suite *s =", module+'_suite();'
    print "    SRunner *sr = srunner_create (s);"
    print "    srunner_run_all (sr, CK_NORMAL);"
    print "    number_failed = srunner_ntests_failed (sr);"
    print "    srunner_free (sr);"
    print "    return (number_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;"
    print "}"
    print "//------------------------------------------------------------"




if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Run like: c_test_generator.py module func1 func2 ...")

    generate_check(sys.argv[1], sys.argv[2:])
