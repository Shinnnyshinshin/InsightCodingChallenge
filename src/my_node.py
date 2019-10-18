
class Node:
    def __init__(self, border, date, measure, value):    
        if border is ot 
        self.border = border
        self.date = date

        self.measure = measure
        self.value = int(value)
        self.set_total_entries = int(value)
        self.set_running_average = 0



    def __getitem__(self, key):
        """Return _nodes[key]"""
        try:
            return self._nodes[key]
        except KeyError:
            raise ("Node '%s' is not in the tree" % key)

    def __setitem__(self, key, item):
        """Set _nodes[key]"""
        self._nodes.update({key: item})



    def get_border(self):
        return self.border

    def set_border(self, x):
        if x is not None:
            self.border = x
        else:
            raise ValueError("border is missing")

    def get_date(self):
        return self.date

    def set_date(self, x):
        if x is not None:
            self.date = x
        else:
            raise ValueError("date is missing")

    def get_measure(self):
        return self.measure

    def set_measure(self, x):
        if x is not None:
            self.measure = x
        else:
            raise ValueError("measure is missing")

    def get_value(self):
        return self.value

    def set_value(self, x):
        if x is not None:
            self.value = int(x)
        else:
            raise ValueError("value is missing")

    def get_total_entries(self):
        return self.total_entries

    def set_total_entries(self, x):
        if x is not None:
            self.set_total_entries = int(x)
        else:
            raise ValueError("total_entires is missing")

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