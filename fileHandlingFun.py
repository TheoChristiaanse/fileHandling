import os
import numpy as np
# This file is make to take an existing data file and replace it with a new fresh file 
# with new fresh data.
# Code is licensed under MIT license
# T. V. Christiaanse


# This saves a matrix of [nxm] content to a tab spaced out file
def FileSaveMatrix(filename, content):
    with open(filename, "a") as f:
        for line in content:
            f.write(" ".join("{:9.6f}\t".format(x) for x in line))
            f.write("\n")

# this saves one line of content to a file
def FileSave(filename, content):
    with open(filename, "a") as myfile:
        myfile.write(content)

# This refreshes the files content and header.
# if the file does not excist it will make a file for you.
def refreshFile(filename,content,header):
    fN= filename
    try:
        os.remove(fN)
    except IOError:
        print("Making file")
        open(fN, 'a').close()

    FileSave(fN,header)
    FileSaveMatrix(fN,content)

refreshFile(fN,content,header)
