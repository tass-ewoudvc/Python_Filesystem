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
            fields[2:4] = fields[2]+fields[3],  #replace road type and number fields by one combined field
            if len(fields) == 6:
                fields[3:5] = [fields[3][1:]+"."+fields[4][:-1]]  #fuse kilometer mark

        fields[-1] = fields[-1].rstrip('\n')
        cams.append(tuple(fields)) # Make the row a tuple, we don't want it to change by accident

    del(cams[-9:])
    return tuple(cams)  # Make the whole dataset a tuple, we don't want it to change by accident



#pylint: disable=C0301
parser = argparse.ArgumentParser(
    description="Queries input text files for Cameras, based on certain criteria")

parser.add_argument("--cameras", required=True, dest='camera_file',
                    help="A properly formatted file containing locations of cameras")

parser.add_argument("--cameras-in-city", dest='city',
                    help="Queries input files for all cameras in a city")

parser.add_argument("--cameras-on-road", dest='road',
                   help="Queries input files for all cameras on a certain road")

args = parser.parse_args()


# Check if at least one of the query arguments is passed
# Better would be to have argparse check this ...
if args.road==None and args.city==None:
    parser.error("Either --cameras-on-road, --cameras-in-city or combination need to be provided")


with open(args.camera_file) as camfile:
    cameras = parse_cameras(camfile)


def printinfo(cams):
    """Prints information about cams"""
    for cam in cams:
        print("Camera on %s at km %s %s in %s (%s)" %
              (cam[2], cam[3], cam[4], cam[1], cam[0]))
    print("")


if args.city:
    citycams = filter(lambda x: args.city in x[1], cameras)
    print("Cameras in", args.city)
    printinfo(citycams)


if args.road:
    roadcams = filter(lambda x: args.road in x[2], cameras)

    print("Cameras on", args.road)
    printinfo(roadcams)
