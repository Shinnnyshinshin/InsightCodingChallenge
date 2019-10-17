

"""

Port Name,State,Port Code,Border,Date,Measure,Value
Metaline Falls,Washington,3025,US-Canada Border,06/01/2019 12:00:00 AM,Buses,7


1. Sum the total number of crossings (Value) of each type of vehicle or equipment, 
or passengers or pedestrians, that crossed the border that month,
regardless of what port was used.

2. Calculate the running monthly average of total crossings, 
rounded to the nearest whole number,  for that combination of 
Border and Measure, or means of crossing.

# this is the second part 
How do we sort? 
The lines should be sorted in descending order by
Date
Value (or number of crossings)
Measure
Border

"""

import json
#import datetime
from dateutil import parser
import hashlib
import math
#import helpers


class EntryCollection:
    def __init__(self):
        #"HASH FUNCTION" : [ Object _ : running count, running average, whatever more values that we need here]
        self.entrydict = {}
    def hash_me(self, entry):
        pass

    def add_entry(self, entry):
        inner_dict = entry.__dict__
        inner_dict["TotalEntries"] = inner_dict['value']

        # the two levels of hashes
        top_hash = inner_dict['border'] + inner_dict['measure']
        mid_hash = inner_dict['date']

        # brand new border and measure combination
        # a lot of people do this don't they?

        if top_hash in self.entrydict:
        # new date combination
            mid_dict = self.entrydict[top_hash]
            # update entry with new
            if mid_hash in mid_dict:
                ref_dict = mid_dict[mid_hash]
                current_count = ref_dict["TotalEntries"]
                ref_dict["TotalEntries"] = inner_dict['value'] + current_count
                # update the lowest level
                mid_dict[mid_hash] = ref_dict
                self.entrydict[top_hash] = mid_dict
            else:
                inner_dict.pop('value')
                mid_dict[mid_hash] = inner_dict
                self.entrydict[top_hash] = mid_dict
        else: 
            # brand new border and measure combination
            mid_to_insert = {}
            inner_dict.pop('value')
            mid_to_insert[mid_hash] = inner_dict 
            self.entrydict[top_hash] = mid_to_insert


class Entry:
    def __init__(self, border="", date="", measure="", value=""):    
        #self.port_name = port_name
        #self.state = state
        #self.port_code = int(port_code)
        self.border = border
        self.date = date # is this a way to do this more efficiently 
        self.measure = measure
        self.value = int(value)
        self.converted_date = self._convert_date(date)
    # check each of the variables
    def _check_port_name(self, port_name):
        pass

    def _check_value(self, value):
        pass

    def _check_measure(self, measure):
        # there are a few different ways : Personal Vehicle / personal Vehicle passengers (REGEX)
        pass
    
    def _convert_date(self, date):
        try:
            mydate = parser.parse(date)
        except:
            return "null"
        return mydate


# this is for the strange way that python 3.7 does the rounding
def myround(numtoRound):
    if numtoRound - math.floor(numtoRound >= 0.5):
        return math.ceil(numtoRound)
    else:
        return math.floor(numtoRound)

def main():
    AllEntries = EntryCollection()
    #file_name = "/Users/willshin/Development/InsightCodingChallenge/input/Stage1.csv"
    file_name = "/Users/willshin/Development/InsightCodingChallenge/input/Border_Crossing_Entry_Data_first100.csv"
    f = open(file_name)
    header = f.readline()
    for line in f.readlines():
        line_fields = line.strip().split(",")
        myEntry = Entry(line_fields[3], line_fields[4], line_fields[5], line_fields[6])
        AllEntries.add_entry(myEntry)

    
    ListOfAllEntries = AllEntries.entrydict
    #print(ListOfAllEntries)
    # add the averages

    # let's sort and do an average first

    current_border_types = ListOfAllEntries.keys()
    for current_border_type in current_border_types:
        current_dates = ListOfAllEntries[current_border_type]
        current_dates_list = sorted(current_dates, reverse=False)
        
        number_seen = 0
        running_total = 0
        prev_total = 0
        # loop through dates and make running average
        for current_date in current_dates_list:
            # running total
            current_entry_dict = ListOfAllEntries[current_border_type][current_date]
            running_total += prev_total
            prev_total = current_entry_dict['TotalEntries']
            if number_seen >= 1:
                #current_entry_dict['TotalAverage'] = round(running_total / number_seen, ndigits=None)
                current_entry_dict['TotalAverage'] = myround(running_total / number_seen)
                number_seen += 1
            else:
                current_entry_dict['TotalAverage'] = 0
                number_seen += 1
            ListOfAllEntries[current_border_type][current_date] = current_entry_dict
    

    FinalListOfDictionaries = []
    current_border_types = ListOfAllEntries.keys()
    print (ListOfAllEntries)
    for current_border_type in current_border_types:
        current_dates_list = ListOfAllEntries[current_border_type]
        for current_date in current_dates_list:
            # running total
            current_entry_dict = ListOfAllEntries[current_border_type][current_date]
            FinalListOfDictionaries.append(current_entry_dict)
    #print (FinalListOfDictionaries)
    FinalListOfDictionaries = sorted(FinalListOfDictionaries, key = lambda i: (i['date'], i['TotalEntries'], i['measure'], i['border']), reverse=True)

    print ('Border,Date,Measure,Value,Average')
    for i in FinalListOfDictionaries:
        # Border,Date,Measure,Value,Average
        print (i['border'] + '\t' + i['date'] + '\t' + i['measure'] + '\t' + str(i['TotalEntries']) + '\t' + str(i['TotalAverage']))
    # output as CSV
    # Date
    # Value (or number of crossings)
    # Measure
    # Border
    # sorted(lis, key = lambda i: (i['age'], i['name'])) 
    #print (FinalListOfDictionaries)
if __name__ == "__main__":
    main()


"""
Questions?  :

set(['Personal Vehicle Passengers', 'Trucks', 'Bus Passengers', 'Pedestrians', 'Rail Containers Empty', 'Buses', 'Personal Vehicles', 'Truck Containers Full', 'Trains', 'Truck Containers Empty', 'Train Passengers', 'Rail Containers Full'])

are bus passengers and busses the same? 
how much varaibility should I take into account

for the dates / all be 1st? or add to month? : soemthign for later

Are all the codes and locations going to match? 
## ok 

To think about : 

Column order switched


{   []
    { []
        {
            [] only one    
        }
    }
}
"""