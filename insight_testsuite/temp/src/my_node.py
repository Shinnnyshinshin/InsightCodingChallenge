
class Node:
    """
        Node class that stores information for each Border, Measure and Date, as well as calculated values. 
    Raises:
        ValueError: Border is missing
        ValueError: Date is missing
        ValueError: Measure is missing
        TypeError: Value cannot be cast as int
        ValueError: Value is missing
        ValueError: Total Entries (calculated value) is missing
    
    """
    def __init__(self, border, date, measure, value):   
        """
            The Node class is a simple object that stores the Border, Date, Measure, Value as well as total entries and running average which was used in the final output. 
            It also inludes necessary getter functions and a method to output the object as a dictionary. 

            Additional consideration was given to the speed of implementation, so most of the error-handling is done when the Node object is constructed, rather than a setter function. 
        
        Arguments:
            border {String} -- Border crossed, passed in from input file
            date {String} -- Date of crossing, passed in from input file
            measure {String} -- Type of crossing, passed in from input file
            value {Integer} -- Number of crossings, passed in from input file
        
        Raises:
            ValueError: Border is missing
            ValueError: Date is missing
            ValueError: Measure is missing
            TypeError: Value cannot be cast as int
            ValueError: Value is missing
            ValueError: Total Entries (calculated value) is missing
        """

        self.border = ""
        self.date = ""
        self.measure = ""
        self.value = ""
        self.total_entries = ""
        self.running_average = 0

        if border is not "":
            self.border = border
        else:
            raise ValueError("border is missing")

        if date is not "":
            self.date = date
        else:
            raise ValueError("date is missing")

        if measure is not "":
            self.measure = measure
        else:
            raise ValueError("measure is missing")

        if value is not "":
            try:
                self.value = int(value)
                self.total_entries = int(value)
            except:
                raise TypeError("value cannot be cast as int")
        else:
            raise ValueError("value is missing")
    
        
    def get_border(self):
        """
            getter for Border
        Returns:
            String -- Border associated with Node. 
        """
        return self.border

    def get_date(self):
        """
            getter for Date
        Returns:
            String -- Date associated with Node. 
        """
        return self.date

    def get_measure(self):
        """
            getter for Measure
        Returns:
            String -- Measure associated with Node. 
        """
        return self.measure

    def get_value(self):
        """
            getter for Value
        Returns:
            String -- Value associated with Node. 
        """
 
        return self.value

    def get_total_entries(self):
        """
            getter for Total Entires
        
        Returns:
            int -- total entries
        """
        return self.total_entries

    def set_running_average(self, x):
        """
            setter for running average
        Arguments:
            x {int} -- current running average to be outputted to file 
        """
        self.running_average = x

    def set_total_entries(self, x):
        """
            setter for Total Entries associated with node. 
        
        Arguments:
            x {int} -- Total Entries for this node. 
        
        Raises:
            ValueError: if total entires is missing
        """
        if x is not None:
            self.total_entries = int(x)
        else:
            raise ValueError("total_entries is missing")

    def as_dict(self):
        """
            Returns Node as dictionary.
        """
        return{
            "border": self.border, 
            "date": self.date,
            "measure": self.measure, 
            "totalentries": self.total_entries, 
            "runningaverage": self.running_average
        }