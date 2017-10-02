
'''
Helper module that checks if unittests have run
By searching a string for a pattern ...
'''
import subprocess, re, os

def check(cwd, files):
    '''Checks if all files run as unit tests'''
    report = {}
    for fi in files:
        try:
            output = subprocess.check_output(["python", os.path.join(cwd, fi)],
                stderr=subprocess.STDOUT,
                universal_newlines=True)
        # Unit tests that fail will also trigger a CalledProcessError
        except subprocess.CalledProcessError as e:
            report[fi] = (False, e.output, e)
        else:
            #report[fi] = check_unittests.check(output)
            report[fi] = True if re.search('Ran.*test', output) else (False, "Didn't see unit test run")
                
    return report


def check_doctest(cwd, files):
    '''Checks if all files run as doc tests'''
    report = {}
    for fi in files:
        try:
            output = subprocess.check_output(["python", os.path.join(cwd, fi)],
                stderr=subprocess.STDOUT,
                universal_newlines=True)
        # Unit tests that fail will also trigger a CalledProcessError
        except subprocess.CalledProcessError as e:
            report[fi] = (False, e.output, e)
        else:
            report[fi] = True
                
    return report


def check_googleTests(cwd, files):
    '''Checks if all files run as google exercises with ok output'''
    report = {}
    for fi in files:
        try:
            output = subprocess.check_output(["python", os.path.join(cwd,fi)],
                stderr=subprocess.STDOUT,
                universal_newlines=True)
        except subprocess.CalledProcessError as e:
            report[fi] = (False, e.output, e)
        else:
            if " X " in output:
                report[fi] = (False, 'One or more tests failed', output)
            else:
                report[fi] = True

    return report

