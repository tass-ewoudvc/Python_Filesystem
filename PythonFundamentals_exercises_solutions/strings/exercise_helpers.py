'''
This file will get automatically copied into the solutions zipfile (all over the place)
'''


import os, glob
import SCons
import subprocess

in_repo = 'isy-academy' in os.getcwd()
if in_repo:
    import course_helpers


gcc = 'gcc'
clang = 'clang'

default_cxxflags = { 
    'clang' : '-std=c++1z -Weverything -Wno-c++98-compat -Wno-c++98-compat-pedantic -Wno-missing-prototypes -Wno-padded -Wno-shadow-field-in-constructor -Wno-weak-vtables -Wno-missing-variable-declarations -Wno-shadow ',

    'gcc' : '-std=c++1z -Wall -Wextra'
}


default_cflags = { 
    'clang' : '-Weverything -std=c99',
    'gcc' : '-Wall -Wextra'
}


def is_gcc(versionstring):
    return 'gcc' in versionstring or 'GCC' in versionstring or 'g++' in versionstring

def typeof_compiler(env):
    '''
    returns you clang or gcc by means of a very dirty check
    '''
    r = subprocess.check_output([env['CXX'],'--version'], stderr=subprocess.STDOUT,)
    
    if 'clang' in r:
        return clang
    elif is_gcc(r):
        return gcc
    else:
        print("typeof_compiler", r)
        raise ValueError('typeof_compiler: unsupported type of compiler: '+r)



def setup_default_cpp_env(env, clang_cxxflags=None, cppflags=None, include_dirs=None):
    '''
    Takes a SCons Environment object, and adds some default configuration to it
    '''
    if in_repo:
        site_scons_dir = os.path.abspath(os.path.join(course_helpers.find_root_directory(), 'site_scons'))
    
        env['ENV'].update({  # for colorgcc, see color gcc manual
            'PATH' : site_scons_dir + os.pathsep + os.environ['PATH'],
        })

    env['ENV'].update({  # for colorgcc, see color gcc manual
        'TERM' : os.environ['TERM'],
        'HOME' : os.environ['HOME']
    })

  
    compiler_type = typeof_compiler(env)
    defaults = default_cxxflags[compiler_type]
    if compiler_type == clang and clang_cxxflags:
        flags = defaults + clang_cxxflags
    elif compiler_type == gcc:
        flags = defaults # + gcc flags
    else:
        flags = defaults
    env.Replace(CXXFLAGS=flags)

    if include_dirs:
        env.Replace(CPPPATH = include_dirs)

    if cppflags:
        env.Replace(CPPFLAGS= cppflags)


def solutions_scons_cpp_setup(env, program_name, run_arguments=None, extra_clang_cxxflags='', extra_cppflags='', extra_libs='', include_dirs=None, files=None):
    '''
    Setups up Scons Environment and targets for a regular C++ solution:
    One that can be built into 'program_name' from all *cpp files in the directory.

    It will also setup SCons to run the program
    run_arguments is a list of command line options (one string per program run)
    So if you'd like to run the program twice with different options, provide me a list of 2
    '''
    setup_default_cpp_env(env, 
                          clang_cxxflags = extra_clang_cxxflags,
                          cppflags = extra_cppflags,
                          include_dirs = include_dirs
                          )
    
    program =env.Program(target = program_name, 
                         source = program_name+'.cpp' if files==None else (files if files!='auto' else glob.glob("*cpp")),
                         LIBS = extra_libs)

    run = None
    runs = None
    if not run_arguments:
        if run_arguments != False: # only None runs the program without arguments, False doesn't run anything
            run = env.Alias('run', program, program[0].abspath)
            env.AlwaysBuild(run)
        else:
            env.Alias('run', None)  # so that the run target exists (CI expects it)
    else:
        runs = []
        for idx, args in enumerate(run_arguments):
            r = env.AlwaysBuild(env.Alias('run{}'.format(idx), 
                                            [program, run] if run else program, 
                                            " ".join((program[0].abspath, args))))
            runs.append(r)

    env.Depends(run, program)
    env.Alias('compile', program) # for when you only want to compile
    if runs:
        env.Alias('run', runs)




def setup_default_c_env(env, clang_cflags=None, cppflags=None, include_dirs=None):
    '''
    Takes a SCons Environment object, and adds some default configuration to it
    '''
    if in_repo:
        site_scons_dir = os.path.abspath(os.path.join(course_helpers.find_root_directory(), 'site_scons'))
    
        env['ENV'].update({  # for colorgcc, see color gcc manual
            'PATH' : site_scons_dir + os.pathsep + os.environ['PATH'],
        })

    env['ENV'].update({  # for colorgcc, see color gcc manual
        'TERM' : os.environ['TERM'],
        'HOME' : os.environ['HOME']
    })

  
    compiler_type = typeof_compiler(env)
    defaults = default_cflags[compiler_type]
    if compiler_type == clang and clang_cflags:
        flags = defaults + clang_cflags
    elif compiler_type == gcc:
        flags = defaults # + gcc flags
    else:
        flags = defaults
    env.Replace(CFLAGS=flags)

    if include_dirs:
        env.Replace(CPPPATH = include_dirs)

    if cppflags:
        env.Replace(CPPFLAGS= cppflags)


def solutions_scons_c_setup(env, program_name, run_arguments=None, extra_clang_cflags='', extra_cppflags='', extra_libs='', include_dirs=None, files=None):
    '''
    Setups up Scons Environment and targets for a regular C solution:
    One that can be built into 'program_name' from all 'program_name.c' or a list of files in the directory.
    Globbing *.c can also be done by passing files='auto'.

    It will also setup SCons to run the program
    run_arguments is a list of command line options (one string per program run)
    So if you'd like to run the program twice with different options, provide me a list of 2

    '''
    setup_default_c_env(env, 
                          clang_cflags = extra_clang_cflags,
                          cppflags = extra_cppflags,
                          include_dirs = include_dirs
                          )
    
    program =env.Program(target = program_name, 
                         source = program_name+'.c' if files==None else (files if files!='auto' else glob.glob("*c")),
                         LIBS = extra_libs)

    run = None
    runs = None
    if not run_arguments: 
        if run_arguments != False:  # only None runs the program without arguments, False doesn't run anything
            run = env.Alias('run', program, program[0].abspath)
            env.AlwaysBuild(run)
        else:
            env.Alias('run', None)  # so that the run target exists (CI expects it)
    else:
        runs = []
        for idx, args in enumerate(run_arguments):
            r = env.AlwaysBuild(env.Alias('run{}'.format(idx), 
                                          [program, run] if run else program, 
                                          " ".join((program[0].abspath, args))))
            runs.append(r)

    env.Depends(run, program)
    env.Alias('compile', program) # for when you only want to compile
    if runs:
        env.Alias('run', runs)

