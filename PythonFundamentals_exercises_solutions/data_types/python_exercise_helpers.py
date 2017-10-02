'''
This file will get automatically copied into the solutions zipfile (all over the place)
'''


import os, glob
import SCons
import subprocess
import hashlib

in_repo = 'isy-academy' in os.getcwd()
if in_repo:
    import course_helpers


def run(env, command, arguments='', outfiles=None):
    abs_command = os.path.abspath(command)
    chmod = env.AlwaysBuild(env.Alias('chmod'+abs_command, [], 'chmod +x ' + abs_command)) 

    if outfiles == None:
        outfiles = [] # not doing this as default parameter, cause we want a fresh list every time this function is called
    elif str == type(outfiles):
        outfiles = [outfiles]

    if not outfiles:  # if there are no other files, hack something with listing *.pyc as output
        # this seems a good trigger if there aren't other outputfiles to this command
        # though SCons seems to crash if you already have output files, to be looked into ..
        outfiles.append(abs_command+'c')  

    fullcommand = " ".join((abs_command, arguments))

    x = env.Alias('run', env.Command(outfiles, [abs_command, chmod], fullcommand))
    env.Clean(x, outfiles)
    return x



def run_with_automatic_redirect(env, command, params):
    '''
    A helper function for running the same program with different arguments
    SCons would normally prevent this, as they all have the same input files,
    and as far as it can tell, they're just aliasses. (Would seem that SCons doesn't look at the actual command of the alias)

    But by adding an artificial output file (using tee) SCons will just run like we expect
    '''
    params = params + ' | tee ' # hacking tee in there, works in combination with outfile below
    outfile = os.path.abspath('.temp'+ hashlib.sha224(command+params).hexdigest()) # short unique output file
    return run(env, command, params+outfile, outfiles=[outfile])



