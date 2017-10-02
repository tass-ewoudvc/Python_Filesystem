

'''
Helper module for coursegrading.py

Examines a participant solution zipfile and produces a report
'''

import os, re, shutil
# my pylint isn't suited for Python3.3 or even 3.x? Hence E1101 disable
#pylint: disable=C0301,E1101

import check_data_types, check_functions, check_modules, check_strings, check_exceptions, check_classes

exercises = {
    'data_types' : check_data_types.files,
    'functions' : check_functions.files,
    'modules' : check_modules.files,
    'strings' : check_strings.files,
    'exceptions' : check_exceptions.files,
    'classes' : check_classes.files,

    # Still refactoring here ;-)
    'iterators' : ('query_cameras.py', ),
    #'exceptions' : ('temperature.py', 'test_temperature.py', 'query_cameras.py', 'camera_parser.py'),
    #'classes' : ('camera_parser.py', 'test_generator.py', 'poweroutlet.py', 'youcontrols.py', 'awesome.py'),
    'user_iterators' : ('camera_parser.py', 'iterators.py'),
    'filesystem' : ('coursegrading.py',)
    #'subprocesses' : ('coursegrading.py', 'examine.py')
    }

exercise_topics = tuple(exercises.keys())

exercise_checkers = {
    'data_types' : check_data_types.check,
    'functions' : check_functions.check,
    'modules' : check_modules.check,
    'strings' : check_strings.check,
    'exceptions' : check_exceptions.check,
    'classes' : check_classes.check,
    }

#---------------------------------------------------------------------
def unpack_solutions(solutions_archive):
    '''
    Helper for examine, unpacks the archive
    Returns the a tuple with a boolean as first, and error or unpack_dir as second
    '''
    # Prepare unpack directory, possibly removing an old one
    base_name = os.path.basename(os.path.abspath(solutions_archive))
    unpack_dir = base_name.split('.')[0]
    #if os.access(unpack_dir, os.F_OK):
    if os.path.exists(unpack_dir):
        shutil.rmtree(unpack_dir)
    os.mkdir(unpack_dir)

    # Unpack
    try:
        shutil.unpack_archive(solutions_archive, unpack_dir)
    except ValueError as v:
        return False, v

    return True, unpack_dir

#---------------------------------------------------------------------
def examine(solutions_archive):
    '''
    Examines the participants solutions directory
    '''
    report = {}

    # Is the name in correct format?
    name_match = re.search(r"[a-zA-Z ]+[-][a-zA-Z ]+[-]PythonFundamentalsSolutions[.]\w",
                           solutions_archive)
    if not name_match:
        report['correct_archivename'] = False
        report['participant_name'] = 'unparsable'
    else:
        report['correct_archivename'] = True
        base_name = os.path.basename(os.path.abspath(solutions_archive))
        names = base_name.split('-')[0:2]
        report['participant_name'] = "{} {}".format(*names)


    #-------------------------------------------------
    # Unpack
    unpack_dir = unpack_solutions(solutions_archive)
    if unpack_dir[0]:
        report['unpack_archive'] = True
        unpack_dir = unpack_dir[1]
    else:
        report['unpack_archive'] = unpack_dir
        #exit('Error: Failed to unpack archive, giving up ...')
        return report
        
    #-------------------------------------------------

    # Check which exercise topics participant zipped
    # Check which topics are lacking
    # Check for stray topics, that aren't in our list
    walked = os.walk(unpack_dir)
    participant_dirs = next(walked)[1]
    participant_topics = tuple(p for p in participant_dirs if p in exercise_topics)
    report['topics'] = participant_topics
    report['lacking_topics'] = tuple(set(exercise_topics) - set(participant_dirs))
    report['stray_topics'] = tuple(p for p in participant_dirs if p not in exercise_topics)

    #-----------------------------------------------------------

    report['exercises_done'] = {}
    report['exercises_lacking'] = {}
    #report['stray_exercise_files'] = {}

    # Check which exercises were done for which module
    for pt in participant_topics:
        expected_files = exercises[pt]
        files = os.listdir(os.path.join(unpack_dir, pt))

        #report['stray_exercise_files'][pt] = set(files) - set(expected_files)
        #print("stray files: ", pt, report['stray_exercise_files'][pt])
        
        report['exercises_done'][pt] = []
        report['exercises_lacking'][pt] = []
        for exfi in expected_files:
            if exfi in files:
                report['exercises_done'][pt].append(exfi)
            else:
                report['exercises_lacking'][pt].append(exfi)

    #-----------------------------------------------------------

    report['checkers'] = {}
    for checker in exercise_checkers:
        report['checkers'][checker] = exercise_checkers[checker](unpack_dir)

    return report
