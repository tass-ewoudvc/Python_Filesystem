#!/usr/bin/python
import os,zipfile
from os import listdir
from os.path import isfile, join
from os import walk

print ("Welcome to this new program in Python, Manolis")
f = []
d = []
for (dirpath, dirnames, filenames) in walk("cfun"):
	f.extend(filenames)
	d.extend(dirnames)
	break

print (*f)
print (*d)

expected = ["classes","data_types","exceptions","functions","modules","strings","iterators","user_iterators","filesystem"]

print(*expected)

found=[]
notfound=[]
for dirname in expected:
	if dirname in d:
		found.append(dirname)
	else:
		notfound.append(dirname)
for elem in found:
	print ("Found", elem)
for elem in notfound:
	print ("Did not find", elem)

