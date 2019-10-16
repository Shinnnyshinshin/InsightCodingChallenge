#
s
    def _convert_date(self, date):
        try:
            mydate = parser.parse(date)
        except:
            return "null"
        return mydate
    
        EntryCollection.add(json.dumps(Entry(line_fields[0], line_fields[1], line_fields[2], line_fields[3], line_fields[4], line_fields[5], line_fields[6] ).__dict__)
        line_fields[0]
        # Port Name, State, Port Code, Border, Date, Measure, Value
        port_name_set.add(line_fields[0])
        state_set.add(line_fields[1])
        port_code_set.add(line_fields[2])
        border_set.add(line_fields[3])
        date_set.add(line_fields[4])
        measure_set.add(line_fields[5])

    print (port_name_set)
    print (state_set)
    print (port_code_set)
    print (border_set)
    print (date_set)
    print (measure_set)




    #string_to_encode = string_to_encode.encode('utf-8')
        #myhash = hashlib.md5(string_to_encode)
        myhash = string_to_encode
        #inner_dict["BorderMeasure"] = inner_dict['border'] + inner_dict['measure']
        # update
        if myhash in self.entrydict:
            #print (myhash)
            ref_dict = self.entrydict[myhash]
            current_count = ref_dict["TotalEntries"]
            ref_dict["TotalEntries"] = inner_dict['value'] + current_count
        # create
        else:
            inner_dict.pop('value')
            self.entrydict[myhash] = inner_dict 


dict_values([
    
    {'US-Canada Border03/01/2019 12:00:00 AMTruck Containers Full': 
    {'border': 'US-Canada Border', 'date': '03/01/2019 12:00:00 AM', 'measure': 'Truck Containers Full', 'converted_date': datetime.datetime(2019, 3, 1, 0, 0), 'TotalEntries': 6483}}, 
    {'US-Canada Border03/01/2019 12:00:00 AMTrains': 
    {'border': 'US-Canada Border', 'date': '03/01/2019 12:00:00 AM', 'measure': 'Trains', 'converted_date': datetime.datetime(2019, 3, 1, 0, 0), 'TotalEntries': 19}}, 
    {'US-Mexico Border03/01/2019 12:00:00 AMPedestrians': 
    {'border': 'US-Mexico Border', 'date': '03/01/2019 12:00:00 AM', 'measure': 'Pedestrians', 'converted_date': datetime.datetime(2019, 3, 1, 0, 0), 'TotalEntries': 346158},
     'US-Mexico Border02/01/2019 12:00:00 AMPedestrians':
    {'border': 'US-Mexico Border', 'date': '02/01/2019 12:00:00 AM', 'measure': 'Pedestrians', 'converted_date': datetime.datetime(2019, 2, 1, 0, 0), 'TotalEntries': 172163},
      'US-Mexico Border01/01/2019 12:00:00 AMPedestrians': 
    {'border': 'US-Mexico Border', 'date': '01/01/2019 12:00:00 AM', 'measure': 'Pedestrians', 'converted_date': datetime.datetime(2019, 1, 1, 0, 0), 'TotalEntries': 56810}}, 
    {'US-Canada Border02/01/2019 12:00:00 AMTruck Containers Empty': 
    {'border': 'US-Canada Border', 'date': '02/01/2019 12:00:00 AM', 'measure': 'Truck Containers Empty', 'converted_date': datetime.datetime(2019, 2, 1, 0, 0), 'TotalEntries': 1319}}])




 # does sorting by date time work?
 # where can we make things more efficient? 
