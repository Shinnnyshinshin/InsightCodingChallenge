# Border Crossing Analysis (By Will Shin)

## Table of Contents
1. [Approach](README.md#Approach)
2. [border_analytics.py](README.md#Main function)
2. [my_node.py](README.md#Node Class)
2. [my_tree.py](README.md#Tree Class)
2. [my_utils.py](README.md#Math Function)

## Approach
The analysis and summary for the border crossing dataset was implemented using a Tree data structure using a set of nested Python dictionaries. The implemention also involved the creation of a Tree and Node class. 

### Main function  (border_analytics.py)
The file handles all of the file I/O, as well creating the main Tree data stucture used. It also handles the reading of the input file, creation of the Nodes, and adding them to the Tree.  

Additional consideration is also given to lines that have missing fields. These lines are not added to the Tree, but are added to a separate list and outputted to the user at the end.  An error message is also printed to the user. 

### Node Class (my_node.py)
The Node class is a simple object that stores the Border, Date, Measure, Value as well as total entries and running average which was used in the final output.  It also inludes necessary getter functions and a method to output the object as a dictionary. 

Additional consideration was given to the speed of implementation, so most of the error-handling is done when the Node object is constructed, rather than a setter function. 

### Tree Class (my_tree.py)
The Tree class handles most of the logic for the Border Crossing analysis, as well as the steps needed to calculate the running average and output csv as sorted list. 

The main "engine" for the class is add_node which is called by the main_function in border_analytics.py, and adds the Node object to the tree. 

In addition to the root node, the Tree objection is comprised of 3 levels. The bottom level is the Node object which contains the Border, Date, Measure, Value and running average fields. It is accessed first from the top levell by a key built from the measure and border values (top_key), and next from the date (mid_key).  By traversing the tree, the Tree is able access all the entries associated with a Border and Measure, by all the Dates that a border crossing occured. 


As a side note, additional consideration was given to how the top_key was constructed (border + measure or measure + border?). Since the number of measures (12) was greater than the number of borders (2), the search for the key was sped up by looking for the measure first. 

After all the nodes are added, then the add_average function then calculates the running average by looping through each measure and border combination, and then loop through each of the dates in chronological order. 

Finally, there is the function as_sorted_list, which traverses all the nodes, compiles them as a sorted list of dictionaries, before return all nodes as a list to be outputted to the final csv file.

### Math Function (my_utils.py)
One additional helper function was needed to over-write python's default rounding behavior. For equally close multiples (ie 0.5) the rounding is done towards the even choice, which is not what we want. The utilities file contains one function that over-writes this default behavior. 



