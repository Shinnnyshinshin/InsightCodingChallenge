
class Node:
    def __init__(self, border, date, measure, value):    

        if border is not "":
            self.border = border
        else:
            raise ValueError("border is missing")

        if date is not None:
            self.date = date
        else:
            raise ValueError("date is missing")

        if measure is not None:
            self.measure = measure
        else:
            raise ValueError("measure is missing")

        if value is not None:
            try:
                self.value = int(value)
            except:
                raise TypeError("value cannot be cast as int")
        else:
            raise ValueError("value is missing")
    
        # non parameter value
        self.total_entries = self.value
        self.running_average = 0 

    def get_border(self):
        return self.border

 #   def set_border(self, x):
 #       if x is not None:
 #           self.border = x
 #       else:
 #           raise ValueError("border is missing")

    def get_date(self):
        return self.date

    def get_measure(self):
        return self.measure

    def set_measure(self, x):
        if x is not None:
            self.measure = x
        else:
            raise ValueError("measure is missing")

    def get_value(self):
        return self.value

    def get_total_entries(self):
        return self.total_entries

    def set_running_average(self, x):
        self.running_average = x

    def set_total_entries(self, x):
        if x is not None:
            self.total_entries = int(x)
        else:
            raise ValueError("total_entries is missing")

    def as_dict(self):
        return{
            "border": self.border, 
            "date": self.date,
            "measure": self.measure, 
            "totalentries": self.total_entries, 
            "runningaverage": self.running_average
        }