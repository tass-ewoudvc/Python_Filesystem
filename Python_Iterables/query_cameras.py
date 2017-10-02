#!/usr/bin/env python

import argparse
import sys

def cameraParsing(cameras):
	my_iter = iter(cameras)
	next(my_iter)
	next(my_iter)
	info = []
	for line in my_iter:
		fields = line.split(',')
		fields[-1] = fields[-1].rstrip('\n')
		info.append(fields)
	del info[-9:]
	print(*info)
	t_info = tuple(info)
	print(type(t_info))
	return t_info

parser = argparse.ArgumentParser(
    description="Queries input text files for Cameras, based on certain criteria")

parser.add_argument("--cameras", required=True, dest='camera_file',
                    help="A properly formatted file containing locations of cameras")

args = parser.parse_args()

with open(args.camera_file) as camfile:
    cameras = cameraParsing(camfile)
    print("HELLOOOOOOOOOOOOOOOO")

def printinfo(cameras):
    """Prints information about cams"""
    for c in cameras:
        print("Camera on %s at km %s %s in %s (%s)" %
              (c[2], c[3], c[4], c[1], c[0]))
    print("")

printinfo(cameras)
