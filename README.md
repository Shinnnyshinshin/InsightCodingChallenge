# Border Crossing Analysis (By Will Shin)

## Table of Contents
1. [Approach](README.md#Approach)
2. [border_analytics.py](README.md#main-function--border_analyticspy)
3. [my_node.py](README.md#node-class-my_nodepy)
4. [my_tree.py](README.md#tree-class-my_treepy)
5. [my_utils.py](README.md#math-function-my_utilspy)
6. [Tests](README.md#Tests)

## Approach
The analysis and summary for the border crossing dataset was implemented using a Tree data structure consisting mainly of a set of nested Python dictionaries. The implemention also involved the creation of a custom Tree and Node class.  


### Main function  (border_analytics.py)
The Main function handles all of the file I/O, as well creating the main Tree data stucture used. It also handles the reading of the input file, creation of the Nodes, and adding them to the Tree.  The main function also calls the necessary Tree class functions to calculate the running average and output the results to the final csv file. 

Additional consideration was also given to lines that have missing fields. These lines are not added to the Tree, but are added to a separate list and outputted to the user at the end.  An error message is also printed to the user. 

### Node Class (my_node.py)
The Node class is a simple object that stores the Border, Date, Measure, Value as well as total entries and running average which was used in the final output csv file.  It also inludes necessary getter functions for the Node object and a method to output the Node object as a dictionary. 

Additional consideration was given to the speed of implementation, so most of the error-handling is done when the Node object is constructed, rather than a setter function. 

### Tree Class (my_tree.py)
The Tree class handles most of the logic for the Border Crossing analysis, as well as the steps needed to calculate the running average and output the Tree object as a sorted list that is used to generate the final csv file. 

The key function for the Tree class is add_node.  This function is called by the main() function in border_analytics.py, and is what adds each Node object to the tree. 

In addition to the ROOT node, the Tree object is comprised of 3 levels. The bottom level is consisted of Node objects which contains the Border, Date, Measure, Value and running average fields for each entry. The Node objects are accessed by traversing the tree, which first cosists of a top level of Measure and Border Values (top_key), and dates associated with each Border-Measur pair (mid_key).
    The Tree class handles the creation of the Tree data struction, the addition of Nodes to the tree, as well as the traversal, averaging and outputting the Tree as a sorted list


As a side note, additional consideration was given to how the top_key was constructed (by concatenating Border + Measure or Measure + Border). Since the number of Measures, or types of crossings (12) was greater than the number of Borders (2), the traversing the tree was sped up by having the top_key built by contatenating Measure + Border. 

After all the Nodes are added,  the add_average() function then calculates the running average by looping through each Measure and Border combination, and then going through each of the Dates in chronological order. 

Finally, there is the function as_sorted_list(), which traverses all the nodes, compiles them as a sorted list of dictionaries, and returns all nodes as a list to be outputted to the final csv file.

### Math Function (my_utils.py)
One additional helper function was needed to over-write Python's default rounding behavior. For equally close multiples (ie 0.5) python performs rounding to the nearest even integer, which is not what we want. The my_utils.py file contains one function that over-writes this default behavior. 

## Tests

There were 3 additional tests that were written for the insight_testsuite folder. One is the Test_emptyfile which reads in an empty file (just the header) and outputs and empty results.csv file (just the header). One is Test_misordered_columns, which tests for the columns being in a different order. There are also two tests that test for missing data (either the border or measure). Both will output the results.csv without the rows containing missing data and output a warning message to the user for each row that was skipped. 