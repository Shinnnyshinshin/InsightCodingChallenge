
import time
import sys
from my_tree import Tree
from my_node import Node


def main():
    """
    The main functions all of the file I/O, as well creating the main Tree data stucture used. 
    The main function handles the reading of the input file, creation of the Nodes, and adding them to the Tree.
    It also calls the necessary functions to calculate the running average and output to final csv file. 

    """
    # needed indices
    header_indices = {"Date": None, "Value": None, "Border": None, "Measure": None}

    if len(sys.argv) < 3:
        print("ERROR: Files are not complete")
        return

    # check if input file and header line exists 
    try:
        infile = sys.argv[1]
        infile_handler = open(infile)
    except OSError:
        print("cannot open", infile)
        return
    else:
        # file should have header
        header = infile_handler.readline()
        header_fields = header.strip().split(',')
        for key in header_indices.keys():
            header_indices[key] = header_fields.index(key)

    # check outfile
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

    all_entries = Tree()
    all_missing_lines = []
    
    # reading files
    while True:
        line = infile_handler.readline()
        if not line:
            break
        line_fields = line.strip().split(",")
        try:
            myNode = Node(line_fields[border_ind], line_fields[date_ind], line_fields[measure_ind],  line_fields[value_ind])
        except ValueError as e:
            print("WARNING: line missing values. skipping")
            print(e)
            all_missing_lines.append(line)
            continue
        all_entries.add_node(myNode)

    # don't forget to close the file handle
    infile_handler.close()

    # calculating the running averages 
    all_entries.add_averages()
    # output as sorted list
    final_list_to_print = all_entries.as_sorted_list()

    outfile_handler.write('Border,Date,Measure,Value,Average\n')
    for line in final_list_to_print:
        outfile_handler.write(line +'\n') 
    outfile_handler.close()


if __name__ == "__main__":
    main()
