
class Node:
    def __init__(self, border="", date="", measure="", value=""):    
        self.border = border
        self.date = date
        self.measure = measure
        self.value = int(value)
        self.total_entries = int(value)
        self.running_average = 0

    def get_border(self):
        return self.border

    def set_border(self, x):
        self.border = x
    
    def get_date(self):
        return self.date

    def set_date(self, x):
        self.date = x

    def get_measure(self):
        return self.measure

    def set_measure(self, x):
        self.measure = x
    
    def get_value(self):
        return self.value

    def set_value(self, x):
        self.value = x
    
    def get_total_entries(self):
        return self.total_entries

    def set_total_entries(self, x):
        self.total_entries = x
    
    def set_running_average(self, x):
        self.running_average = x

    def as_dict(self):
        return{
            "border": self.border, 
            "date": self.date,
            "measure": self.measure, 
            "totalentries": self.total_entries, 
            "runningaverage": self.running_average
        }