

'''
Helper module for coursegrading

Checks all exercises in the functions subdir
'''

import check_unittests, os

files = ('dict_inverse.py','number_tester.py','palindrome.py','transpose.py')

def check(maindir):
    '''
    Checks exercises for the functions subdir
    '''
    # report = {}
    # for fi in files:
    #     try:
    #         output = subprocess.check_output(["python", os.path.join(maindir,'functions',fi)],
    #             stderr=subprocess.STDOUT,
    #             universal_newlines=True)
    #     # Unit tests that fail will also trigger a CalledProcessError
    #     except subprocess.CalledProcessError as e:
    #         report[fi] = (False, e.output, e)
    #     else:
    #         report[fi] = check_unittests.check(output)
                
    # return report
    cwd = os.path.join(maindir,'functions')
    return check_unittests.check(cwd, files)
            
        
