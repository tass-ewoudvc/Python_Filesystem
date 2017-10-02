#!/usr/bin/env python

'''
????

Tass PythonFundamentals course
Solution to: Course grading system
'''
# my pylint isn't suited for Python3.3 or even 3.x? Hence E1101 disable
#pylint: disable=C0301,E1101

import sys, os
from examine import examine

if len(sys.argv) < 2:
    exit("Error: Pass an archive as argument")

solutions_archive = sys.argv[1]

#if not os.access(solutions_archive, os.F_OK):
if not os.path.exists(solutions_archive):
    exit("Error: Could not access file")


report = examine(solutions_archive)

            
#print(report)
print("\nArchive under test: ", solutions_archive)
print("Is {}correctly named, by author: {}\n".format('in' if not report['correct_archivename'] else '',
                                                 report['participant_name']))

print("Found exercise directories:")
for pt in report['topics']:
    print("    ", pt)

print("\nLacking exercise directories:")
for pt in report['lacking_topics']:
    print("    ", pt)

if len(report['stray_topics']):
    print("\nFound stray directories:")
    for pt in report['stray_topics']:
        print("    ", pt)


for pt in report['topics']:
    if len(report['exercises_done'][pt]):
        print("\nFound the following solutions in directory", pt)
        for exd in report['exercises_done'][pt]:
            print("    ", exd)

    if len(report['exercises_lacking'][pt]):
        print("\nDirectory {} lacks the following:".format(pt))
        for exl in report['exercises_lacking'][pt]:
            print("    ", exl)

for checker in report['checkers']:
    print("\nRun Output result for", checker)
    for file,output in report['checkers'][checker].items():
        if output == True:
            print("    ", file, output)
        else:
            print("    ", file, output[1])
    
        
print()

#-----------------------------------------------------------
