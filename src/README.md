# Border Crossing Analysis (By Will Shin)

## Table of Contents
1. [Approach](README.md#Approach)
1. [Additional Considerations](README.md#Additional Considerations)

## Approach
The analysis and summary for the border crossing dataset was implemented using a Tree data structure using a set of nested Python dictionaries. The implemention also involved the creation of a Tree and Node class. 

### Main function  (border_analytics.py)
The file handles all of the file I/O, as well creating the main Tree data stucture used. It also handles the reading of the input file, creation of the Nodes, and adding them to the Tree.  

Additional consideration is also given to lines that have missing fields. These lines are not added to the Tree, but are added to a separate list and outputted to the user at the end.  An error message is also printed to the user. 

### Node Class (my_node.py)
The Node class is a simple object that stores the Border, Date, Measure, Value as well as total entries and running average which was used in the final output.  It also inludes necessary getter functions and a method to output the object as a dictionary. 

Additional consideration was given to the speed of implementation, so most of the error-handling is done when the Node object is constructed, rather than a setter function. 

### Tree Class (my_tree.py)



Additional the order in which the measure was contatenated was determined by the number of border crossings (which was 2) vs the number of measures, which was 12 in the dataset given.


### Math Function (my_utils.py)

* additional considerations



