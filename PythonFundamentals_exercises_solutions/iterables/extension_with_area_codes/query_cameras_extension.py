#!/usr/bin/env python

"""
Queries files from "Agentschap Wegen en Verkeer" for traffic cameras
based on certain criteria

Tass PythonFundamentals course
Solution to: Traffic cameras
"""

import argparse #pylint: disable=F0401
import sys

# line too long
#pylint: disable=C0301

# shadowing variable
#pylint: disable=W0621

# warnings regarding builtin filter and map
# but this is an execise on those ...
#pylint: disable=W0141
#pylint: disable=W0110


def parse_cameras(cameras):
    """Parses an iteratable for cameras
    Parses according to the format of "Agentschap Wegen en Verkeer"
    """
    itercams = iter(cameras)
    next(itercams)  # don't care about the first line
    fmt = next(itercams) # second line contains format
    sep_type = "Type weg" in fmt  #is road type separate from nr?

    cams = []
    for line in itercams:
        fields = line.split(',')
        if sep_type:
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


#pylint: disable=C0301
parser = argparse.ArgumentParser(
    description="Queries input text files for Cameras, based on certain criteria")

parser.add_argument("--cameras", required=True, dest='camera_file',
                    help="A properly formatted file containing locations of cameras")

parser.add_argument("--areacodes", required=True, dest='areacodes_file',
                    help="A properly formatted file containing area codes for cities")

parser.add_argument("--cameras-in-areacode", dest='areacode',
                    help="Queries input files for all cameras in an area code")

parser.add_argument("--cameras-in-city", dest='city',
                    help="Queries input files for all cameras in a city")

parser.add_argument("--cameras-on-road", dest='road',
                   help="Queries input files for all cameras on a certain road")

args = parser.parse_args()

required_either = (args.areacode, args.road, args.city)
either = [arg for arg in required_either if arg ]
if len(either) == 0:
    parser.error("Either --cameras-on-road, --cameras-in-areacode, --cameras-in-city or combination need to be provided")


with open(args.camera_file) as camfile:
    cameras = parse_cameras(camfile)

with open(args.areacodes_file) as areafile:
    areacodes = parse_areacodes(areafile)


def printinfo(cams):
    """Prints information about cams"""
    for cam in cams:
        print("Camera on %s at km %s %s in %s (%s)" %
              (cam[2], cam[3], cam[4], cam[1], cam[0]))
    print("")


if args.areacode:
    cities = set(map(lambda x: x[3],
                     filter(lambda x: args.areacode in x, areacodes)))
    if len(cities) > 1:
        sys.exit("Error: Multiple head-cities with same area code?")

    city = tuple(cities)[0]
    areacams = filter(lambda x: city in x[1], cameras)

    print("Cameras in %s %s" % (args.areacode, city))
    printinfo(areacams)

if args.city:
    citycams = filter(lambda x: args.city in x[1], cameras)
    codes = set(map(lambda x: x[2],
                       filter(lambda x: args.city == x[3], areacodes)))

    areacode = tuple(codes)[0]
    print("Cameras in %s %s" % (areacode, args.city))
    printinfo(citycams)


if args.road:
    roadcams = filter(lambda x: args.road in x[2], cameras)

    print("Cameras on " + args.road)
    printinfo(roadcams)
