#!/usr/bin/env python

"""
Tass PythonFundamentals Course
Solution to: "Piglatin"
"""

import sys

def to_piglatin(string, hyphonate=False):
    """ Converts a string to piglatin """
    # This could be done more performant using a list and join()
    ret = []
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for word in string.split():
        if word[0] in vowels:
            ret.append("%s%s%s" % (word,
                                   "-" if hyphonate else "",
                                   "way"))
        else:
            first_cosonant_idx = 0
            while ( first_cosonant_idx < len(word)
                and word[first_cosonant_idx] not in vowels):
                first_cosonant_idx += 1

            ret.append("%s%s%s%s" % (word[first_cosonant_idx:],
                                    "-" if hyphonate else "",
                                    word[:first_cosonant_idx],
                                    "ay"))
    return " ".join(ret)



def from_piglatin(string):
    """ Converts a string from piglatin """
    ret = []
    for word in string.split():
        hyphen_idx = word.find('-')
        if "way" == word[-3:]:
            word = word[:-3]
        else:
            word = word[:-2]

        ret.append(word[hyphen_idx+1:] + word[:hyphen_idx])

    return " ".join(ret)



if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Need 2 parameters")

    with open(sys.argv[1]) as fin:
        with open(sys.argv[2], "w") as fout:
            for line in fin:
                fout.writelines(to_piglatin(line))
