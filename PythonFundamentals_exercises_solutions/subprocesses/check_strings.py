
'''
Helper module for coursegrading

Checks all exercises in the strings subdir
'''
import os, check_unittests

unittestable_files = ('test_piglatin.py',)
googletest_files = ('wordcount.py', 'mimic.py')
other_files = ('piglatin.py', 'test_generator.py', 'c_test_generator.py')
files = tuple(list(unittestable_files) + list(googletest_files) + list(other_files))

def check(maindir):
    '''
    Checks exercises for the strings subdir
    '''
    report = {}
    cwd = os.path.join(maindir,'strings')
    if not os.path.exists(cwd) :
        report['Error'] = (False, 'strings not found')
        return report

    report.update(check_unittests.check(cwd, unittestable_files))
    report.update(check_unittests.check_googleTests(cwd, googletest_files))

    # Add checks for the refactored code generator and c code generator!

    return report
