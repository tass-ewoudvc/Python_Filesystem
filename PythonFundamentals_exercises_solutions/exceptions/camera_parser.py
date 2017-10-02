#!/usr/bin/env python

"""
Parses from "Agentschap Wegen en Verkeer"
Parses Area codes files

Tass PythonFundamentals course
Solution to: Traffic cameras refactoring
"""

import doctest #pylint: disable=F0401

# line too long
#pylint: disable=C0301

def parse_cameras(cameras):
    """Parses an iteratable for cameras
    Parses according to the format of "Agentschap Wegen en Verkeer"

    >>> parse_cameras([None, 'Type weg', 'West-Vlaanderen,Koksijde,N,396,"5,000",'] + [','*7]*9)
    (('West-Vlaanderen', 'Koksijde', 'N396', '5.000', ''),)

    >>> parse_cameras([None, 'Type weg', 'West-Vlaanderen,Brugge,R,30,"2,475",Richting Oostende'] + [','*7]*9)
    (('West-Vlaanderen', 'Brugge', 'R30', '2.475', 'Richting Oostende'),)

    >>> parse_cameras([None, '', 'West-Vlaanderen,Staden,N 36,,5.15,richting Zarren'] + [','*7]*9)
    (('West-Vlaanderen', 'Staden', 'N 36', '', '5.15', 'richting Zarren'),)

    >>> parse_cameras([None, '', 'West-Vlaanderen,Kortrijk,N 43,,"45,1??",'] + [','*7]*9)
    (('West-Vlaanderen', 'Kortrijk', 'N 43', '', '"45', '1??"', ''),)

    Bad case scenario:
    >>> parse_cameras([None, 'Type weg', 'West-Vlaanderen,Koksijde,N,396,"5'] + [','*7]*9)
    Traceback (most recent call last):
    Exception: Wrong number of fields

    """
    itercams = iter(cameras)
    next(itercams)  # don't care about the first line
    fmt = next(itercams) # second line contains format
    sep_type = "Type weg" in fmt  #is road type separate from nr?

    cams = []
    for line in itercams:
        fields = line.split(',')
        if sep_type:
            if len(fields) < 6 : raise Exception("Wrong number of fields")
            fields[2:4] = fields[2]+fields[3],  #cat road type and number
            if len(fields) == 6:
                fields[3:5] = [fields[3][1:]+"."+fields[4][:-1]]  #fuse kilometer mark

        fields[-1] = fields[-1].rstrip('\n')
        cams.append(tuple(fields))

    del(cams[-9:])
    return tuple(cams)



def parse_areacodes(areacodes):
    """
    Parses an iterable for area codes
    Parses according to the format on http://postcodezoeker.be/Postcodes.php
    """
    itercodes = iter(areacodes)
    next(itercodes) # don't care about first 2 lines
    next(itercodes)

    codes = []
    for line in itercodes:
        codes.append(tuple(line.split(',')))

    return tuple(codes)



if __name__ == "__main__":
    doctest.testmod()
