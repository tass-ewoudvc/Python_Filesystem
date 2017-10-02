

'''
Helper module for coursegrading

Checks all exercises in the strings subdir
'''

import subprocess
import os, sys, check_unittests

files = ('string1.py', 'string2.py', 'list1.py', 'list2.py')

def check(maindir):
    '''
    Checks exercises for the strings subdir
    '''
    #report = {}
    # for fi in files:
    #     try:
    #         output = subprocess.check_output(["python", os.path.join(maindir,'data_types',fi)],
    #             stderr=subprocess.STDOUT,
    #             universal_newlines=True)
    #     except subprocess.CalledProcessError as e:
    #         report[fi] = (False, e, e.output)
    #     else:
    #         if " X " in output:
    #             report[fi] = (False, 'One or more tests failed', output)
    #         else:
    #             report[fi] = True

    # return report
    cwd = os.path.join(maindir,'data_types')
    return check_unittests.check_googleTests(cwd, files)
        
