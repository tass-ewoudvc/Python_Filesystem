
'''
Helper module for coursegrading

Checks all exercises in the exceptions subdir
'''
import os, check_unittests

unittestable_files = ('test_temperature.py',)
doctesttable_files = ('camera_parser.py',)
other_files = ('temperature.py', 'query_cameras.py',)
files = tuple(list(unittestable_files) + list(doctesttable_files) + list(other_files))

def check(maindir):
    '''
    Checks exercises for the exceptions subdir
    '''
    report = {}
    cwd = os.path.join(maindir,'exceptions')
    if not os.path.exists(cwd) :
        report['Error'] = (False, 'exceptions not found')
        return report

    report.update(check_unittests.check(cwd, unittestable_files))
    report.update(check_unittests.check_doctest(cwd, doctesttable_files))

    return report
