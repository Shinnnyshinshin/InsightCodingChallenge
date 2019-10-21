#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Belw is an example of what might be found in this file if your program was written in Python 3.7
# python3.7 ./src/border_analytics.py ./input/Border_Crossing_Entry_data.csv ./output/report.csv


# this is the final version : rewrite to not do the test file thing
#python ./src/border_analytics.py ./input/Border_Crossing_test.csv ./output/report.csv
python3.7 ./src/border_analytics.py ./input/Border_Crossing_Entry_Data.csv ./output/report.csv
#python ./src/border_analytics.py ./input/Border_Crossing_missing.csv ./output/report.csv
