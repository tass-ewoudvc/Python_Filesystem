

'''
Helper module for coursegrading

Checks all exercises in the modules subdir
'''

import subprocess
import os, sys, stat

files = ('temperature.py', 'test_temperature.py', 'test_generator.py', 'c_test_generator.py', 'makefile', 'check_dummy.c')

def check(maindir):
    '''
    Checks exercises for the modules subdir
    '''
    cwd = os.path.join(maindir,'modules')
    report = {}

    if not os.path.exists(cwd) :
        report['Error'] = (False, 'modules not found')
        return report

    # Temperature
    name = files[1]
    try:
        output = subprocess.check_output(["python", os.path.join(cwd, name)],
                    stderr=subprocess.STDOUT,
                    universal_newlines=True)
        
    # Unit tests that fail will also trigger a CalledProcessError
    except subprocess.CalledProcessError as e:
        report[name] = (False, e.output, e)
    else:
        if "OK" in output:
            report[name] = True
        else:
            report[name] = (False, output)


    # Should add a test for test_generator.py, but need to copy a python file from somewhere else here
    # Or: copy temperature.py to another name, run test_generator.py, save the output, and run its tests

    # C test generator
    name = files[3]
    try:
        output = subprocess.check_output(['make','clean', 'check_dummy'],
                    cwd=cwd,
                    stderr=subprocess.STDOUT,
                    universal_newlines=True)

        checkfile = os.path.join(cwd, 'check_dummy')
        # set correct file permissions
        filemode = os.stat(checkfile).st_mode
        os.chmod(checkfile, stat.S_IEXEC | filemode)
        
        output = subprocess.check_output(checkfile,
                    stderr=subprocess.STDOUT,
                    universal_newlines=True)
        
    # Unit tests that fail will also trigger a CalledProcessError
    except subprocess.CalledProcessError as e:
        # The check_ executable must faill all unit tests!
        if "Assertion '0' failed" in e.output:
            report[name] = True         
        else:
            report[name] = (False, e.output, e)
            
    return report
            
        
