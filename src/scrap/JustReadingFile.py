# Just reading file
import json
#import datetime
from dateutil import parser
import hashlib
import math



def main():
    #file_name = "/Users/willshin/Development/InsightCodingChallenge/input/Stage1.csv"
    measure_set = set()
    file_name = "/Users/willshin/Development/InsightCodingChallenge/input/Border_Crossing_Entry_Data.csv"
    f = open(file_name)
    header = f.readline()
    date_set = set()
    measure_set = set()
    for line in f.readlines():
        line_fields = line.strip().split(",")
        measure_set.add(line_fields[5])

    print(len(measure_set))
if __name__ == "__main__":
    main()


