# Just reading file
import json
#import datetime
from dateutil import parser
import hashlib
import math



def main():
    #file_name = "/Users/willshin/Development/InsightCodingChallenge/input/Stage1.csv"
    file_name = "/Users/willshin/Development/InsightCodingChallenge/input/Border_Crossing_Entry_Data.csv"
    f = open(file_name)
    header = f.readline()
    date_set = set()
    measure_set = set()
    for line in f.readlines():
        line_fields = line.strip().split(",")
        date_set.add(line_fields[4])
        measure_set.add(line_fields[5])


    for measure in measure_set:
        print(measure)
if __name__ == "__main__":
    main()


