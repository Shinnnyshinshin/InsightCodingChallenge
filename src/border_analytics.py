
import time
import json
import sys
from dateutil import parser
import hashlib
import math

import myutils
from mytree import Tree
from mynode import Node


# tree to contain all
AllEntries = None

def main():
    
    # needed indices

    header_indices = {"Date":None, "Value":None, "Border":None, "Measure":None}

    # check if all input files are there
    if len(sys.argv) < 3:
        print("ERROR: Files are not complete")
        #raise IndexError("Files Missing")
        return

    # check files 
    try:
        infile = sys.argv[1]
        infile_handler = open(infile)
    except OSError:
        print("cannot open", infile)
    else:
        # file should have header
        header = infile_handler.readline()
        header_fields = header.strip().split(',')
        for key in header_indices.keys():
            header_indices[key] = header_fields.index(key)

    # check outfile early-on too 
    try:
        outfile = sys.argv[2]
        outfile_handler = open(outfile, 'w')
    except OSError:
        print("cannot open", outfile)


    # if anything is not right
    if None in header_fields:
        print("ERROR: Needed fields do not exist in input file")    
        return

    # store them once
    border_ind = header_indices["Border"]
    date_ind = header_indices["Date"]
    measure_ind = header_indices["Measure"]
    value_ind = header_indices["Value"]

    AllEntries = Tree()
    # reading files
    while True:
        line = infile_handler.readline()
        if not line:
            break
        line_fields = line.strip().split(",")
        myNode = Node(line_fields[border_ind], line_fields[date_ind], line_fields[measure_ind],  line_fields[value_ind])
        AllEntries.add_node(myNode)

    # don't forget
    infile_handler.close()

    # calculating the running averages 
    AllEntries.add_averages()
    # output as sorted list

    FinalListToPrint = AllEntries.as_sorted_list()
    
    outfile_handler.write('Border,Date,Measure,Value,Average\n')
    for line in FinalListToPrint:
        print (line)
        outfile_handler.write(line +'\n') 
    outfile_handler.close()


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
