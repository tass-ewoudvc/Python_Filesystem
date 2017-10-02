
'''
Helper module for coursegrading

Checks all exercises in the classes subdir
'''
import os, check_unittests

unittestable_files = ('test_poweroutlet.py', 'test_awesome.py', 'test_youcontrols.py')
doctesttable_files = ('camera_parser.py',)
other_files = ('query_cameras.py', 'test_generator.py', 'poweroutlet.py', 'awesome.py', 'youcontrols.py')
files = tuple(list(unittestable_files) + list(doctesttable_files) + list(other_files))

def check(maindir):
    '''
    Checks exercises for the classes subdir
    '''
    report = {}
    cwd = os.path.join(maindir,'classes')
    if not os.path.exists(cwd) :
        report['Error'] = (False, 'classes not found')
        return report

    report.update(check_unittests.check(cwd, unittestable_files))
    report.update(check_unittests.check_doctest(cwd, doctesttable_files))

    return report
