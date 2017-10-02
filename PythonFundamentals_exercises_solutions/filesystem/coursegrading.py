#!/usr/bin/env python

'''
????

Tass PythonFundamentals course
Solution to: Course grading system
'''
# my pylint isn't suited for Python3.3 or even 3.x? Hence E1101 disable
#pylint: disable=C0301,E1101

import sys, os, re, shutil

if len(sys.argv) < 2:
    exit("Error: Pass an archive as argument")


# def print_report(rep):
#     '''
#     Prints a report of the solutions screening
#     (rep is expected to be a dict)
#     '''
#     print(rep)


solutions_archive = sys.argv[1]

#if not os.access(solutions_archive, os.F_OK):
if not os.path.exists(solutions_archive):
    exit("Error: Could not access file")

report = {}

#-----------------------------------------------------------

# Is the name in correct format?
name_match = re.search(r"[a-zA-Z ]+[-][a-zA-Z ]+[-]PythonFundamentalsSolutions[.]\w",
                       solutions_archive)
if not name_match:
    report['correct_archivename'] = False
    report['participant_name'] = 'unparsable'
else:
    report['correct_archivename'] = True
    names = solutions_archive.split('-')[0:2]
    report['participant_name'] = "{} {}".format(*names)

#-----------------------------------------------------------
    
# Prepare unpack directory, possibly removing an old one
unpack_dir = solutions_archive.split('.')[0]
#if os.access(unpack_dir, os.F_OK):
if os.path.exists(unpack_dir):
    shutil.rmtree(unpack_dir)
os.mkdir(unpack_dir)

# Unpack
try:
    shutil.unpack_archive(solutions_archive, unpack_dir)
except ValueError as v:
    report['unpack_archive'] = (False, v)
    print(report)
    exit('Error: Failed to unpack archive, giving up ...')
else:
    report['unpack_archive'] = True

#-----------------------------------------------------------


exercises = {
    'modules' : ('temperature.*py$', 'test_generator.py$', 'c_test_generator.py$'),
    'exceptions' : ('temperature.*py$', 'camera.*py$'),
    'functions' : ('dict.*inverse.*py$','number.*tester.*py$','palindrome.*py$','transpos.*py$'),
    'iterators' : ('camera.*py$', ),
    'strings' : ('piglatin.*.py$', 'generator.*py$', 'wordcount.*py$', 'mimic.*py$'),
    'user_iterators' : ('camera.*py$', 'iterators.*py$'),
    'classes' : ('camera.*py$', 'generator.*py$', 'outlet.*py$'),
    'filesystem' : ('grading.*py$',)
    }

exercise_topics = tuple(exercises.keys())


# Check which exercise topics participant zipped
# Check which topics are lacking
# Check for stray topics, that aren't in our list
walked = os.walk(unpack_dir)
participant_dirs = next(walked)[1]
participant_topics = tuple([p for p in participant_dirs if p in exercise_topics])
report['topics'] = participant_topics
report['lacking_topics'] = tuple(set(exercise_topics) - set(participant_dirs))
report['stray_topics'] = tuple([p for p in participant_dirs if p not in exercise_topics])

#-----------------------------------------------------------

#compile the regexes
exercises_regexes = { name : tuple([re.compile(ex) for ex in exercises[name]]) for name in exercises }
report['exercises_done'] = {}
report['exercises_lacking'] = {}

# Check which exercises were done for which module
for pt in participant_topics:
    regexes = exercises_regexes[pt]
    files = os.listdir(os.path.join(unpack_dir, pt))
    report['exercises_done'][pt] = []
    report['exercises_lacking'][pt] = []
    for rex in regexes:
        exes_done = tuple([ex for ex in files if rex.search(ex)])
        #print(pt, rex.pattern, "---", exes_done, files)
        if exes_done:            
            report['exercises_done'][pt] += exes_done
        else:
            report['exercises_lacking'][pt].append(rex.pattern)


#print(report)
print("\nArchive under test: ", solutions_archive)
print("Is {}correctly named, by author: {}\n".format('in' if not report['correct_archivename'] else '',
                                                 report['participant_name']))

print("Found exercise directories:")
for pt in participant_topics:
    print("    ", pt)

print("\nLacking exercise directories:")
for pt in report['lacking_topics']:
    print("    ", pt)

if len(report['stray_topics']):
    print("\nFound stray directories:")
    for pt in report['stray_topics']:
        print("    ", pt)


for pt in participant_topics:
    if len(report['exercises_done'][pt]):
        print("\nFound the following solutions in directory", pt)
        for exd in report['exercises_done'][pt]:
            print("    ", exd)

    if len(report['exercises_lacking'][pt]):
        print("\nDirectory {} lacks the following (nothing matches these patterns):".format(pt))
        for exl in report['exercises_lacking'][pt]:
            print("    ", exl)
        
print()
