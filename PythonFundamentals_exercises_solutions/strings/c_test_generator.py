#!/usr/bin/env python

"""
Generates runnable C skeleton code to UnitTest a module using Check

Can also run as a program, with arguments being header files to create test for

Tass PythonFundamentals course
Solution to: Refactor C UnitTest generator program
"""

import sys
import re


def generate_check(module, functions):
    """Generates skeleton C code for a Check UnitTest"""
    ret = []
    ret.append('''//Automatically generated code to Check module {0}

#include <stdlib.h>
#include <check.h>
#include "{0}.h"
//------------------------------------------------------------
'''.format(module))

    for func in functions:
        ret.append('''START_TEST (test_{0})
{{
    ck_abort();
}}
END_TEST
//------------------------------------------------------------
'''.format(func))

    ret.append('''Suite* {0}_suite()
{{
    Suite* s = suite_create("{0}");
    TCase* core = tcase_create("Core");
'''.format(module))

    for func in functions:
        ret.append('''    tcase_add_test(core, test_{0});\n'''.format(func))

    ret.append('''    suite_add_tcase(s, core);
    return s;
}
//------------------------------------------------------------
''')

    ret.append("""int main()
{{
    int number_failed;
    Suite *s ={0}_suite();
    SRunner *sr = srunner_create (s);
    srunner_run_all (sr, CK_NORMAL);
    number_failed = srunner_ntests_failed (sr);
    srunner_free (sr);
    return (number_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
}}
//------------------------------------------------------------
""".format(module))

    return "".join(ret)



def parse_header(fin):
    """
    Parses function declarations in a header

    fin is a open file object
    """
    pattern = re.compile(r"[a-zA-Z]+ +(.+)\(.+\);")
    ret = []
    for line in fin:
        name = pattern.findall(line)
        ret += name
    return tuple(ret)




if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Run like: c_test_generator.py header1.h header2.h ...")

    for header in sys.argv[1:]:
        with open(header) as headerfile:
            funcs = parse_header(headerfile)

        mod = header[:-2]
        with open("check_"+mod+".c", "w") as fout:
            fout.write(generate_check(mod, funcs))
