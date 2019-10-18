
import time
import json
import sys
from dateutil import parser
import hashlib
import math


AllEntryCollection = None


class EntryCollection:
    """
        This collection o f
    """
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
    
    def keys(self):
        return self.entrydict.keys()


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
    
    # prepare to read all lines
    AllEntryCollection = EntryCollection()
    
    # store them once
    border_ind = header_indices["Border"]
    date_ind = header_indices["Date"]
    measure_ind = header_indices["Measure"]
    value_ind = header_indices["Value"]
    

    # reading files
    while True:
        line = infile_handler.readline()
        if not line:
            break
        line_fields = line.strip().split(",")
        myEntry = Entry(line_fields[border_ind], line_fields[date_ind], line_fields[measure_ind],  line_fields[value_ind])
        AllEntryCollection.add_entry(myEntry)
    # don't forget
    infile_handler.close()



    

    ListOfAllEntries = AllEntryCollection.entrydict
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
    for current_border_type in current_border_types:
        current_dates_list = ListOfAllEntries[current_border_type]
        for current_date in current_dates_list:
            # running total
            current_entry_dict = ListOfAllEntries[current_border_type][current_date]
            FinalListOfDictionaries.append(current_entry_dict)
    #print (FinalListOfDictionaries)
    FinalListOfDictionaries = sorted(FinalListOfDictionaries, key = lambda i: (i['date'], i['TotalEntries'], i['measure'], i['border']), reverse=True)

    
    outfile_handler.write('Border,Date,Measure,Value,Average\n')
    for i in FinalListOfDictionaries:
        # Border,Date,Measure,Value,Average
        outfile_handler.write(i['border'] + ',' + i['date'] + ',' + i['measure'] + ',' + str(i['TotalEntries']) + ',' + str(i['TotalAverage']) +'\n')
    
    
    outfile_handler.close()
    # exit gracefully
    sys.exit(0)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
