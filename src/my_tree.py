#!/usr/bin/env python

from my_node import Node
from my_utils import myround

class Tree(object):
    """Tree objects are made of Node(s) stored in a dictionary called _nodes. 

    It consists of a ROOT, as well as additional levels. 

    The bottom level is consisted of Node objects, which correspond to a Measure and Border pair along with the assoiated Date of entry
    The next level up is consisted of Date strings, and the next level is the Meausre and Border pair

    Thus by traversing the tree, the program is able to quickly access each Node along with Measure, Border and Date associated with the Node. 

    The Tree class handles the creation of the Tree data struction, the addition of Nodes to the tree, as well as the traversal, averaging and outputting the Tree as a sorted list
    """

    def __init__(self):
        """
            Initiate a new Tree and add Root node
        """
        self._nodes = {}
        self._add_root()
    
    def _add_root(self):
        """
            Add ROOT to tree. 
        """
        self._nodes["ROOT"] = {}

    def _top_tree(self):
        """
        Returns top_key level dictionary, which describes the Measure and Border. 
        
        Returns:
            dict -- a dictionary containing th
        """
        return self._nodes["ROOT"]

    def _add_node_to_tree(self, top_key, mid_key, node):
        """
            Private function to add new Node to tree.
        
        Arguments:
            top_key {string} -- Measure and Border to add
            mid_key {string} -- Date to add
            node {Node} -- Node object to add
        """
        mid_tree = {}
        mid_tree[mid_key] = node
        self._top_tree()[top_key] = mid_tree

    def _update_node_to_tree(self, top_key, mid_key, node):
        """
            Private function to update Node in tree.
    
        Arguments:
            top_key {string} -- Measure and Border to update
            mid_key {string} -- Date to update
            node {Node} -- Node object to update
        """
        self._top_tree()[top_key][mid_key] = node

    def add_node(self, node):
        """
            Determines if Node will be added or updated. Performs addition or update.
        
        Arguments:
            node {Node} -- Node object to be added to tree
        """
        top_key = node.get_measure() + node.get_border()
        mid_key = node.get_date()

        if top_key in self._top_tree():
        # new date combination
            mid_tree = self._top_tree()[top_key]
            # update node
            if mid_key in mid_tree:
                ref_node = mid_tree[mid_key]
                current_count = ref_node.get_total_entries()
                ref_node.set_total_entries(node.get_value() + current_count)
                self._update_node_to_tree(top_key, mid_key, ref_node)
            # add node
            else:
                self._update_node_to_tree(top_key, mid_key, node)
        else: 
            # brand new entry
            self._add_node_to_tree(top_key, mid_key, node)

    def add_averages(self):
        """
            Traverses the tree and calculates running average to be outputted to final CSV file
        """
        all_top_keys = self._top_tree().keys()
        for top_key in all_top_keys:
            # sort dates
            current_dates = self._top_tree()[top_key]
            current_dates_list = sorted(current_dates, reverse=False)
            number_seen = 0
            running_total = 0
            prev_total = 0
            # loop through dates and calculate running average
            for current_date in current_dates_list:
                current_node = self._top_tree()[top_key][current_date]
                running_total += prev_total
                prev_total = current_node.get_total_entries()
                if number_seen >= 1:
                    current_node.set_running_average(myround(running_total / number_seen))
                    number_seen += 1
                else:
                    number_seen += 1
                self._update_node_to_tree(top_key, current_date, current_node)
    
    def as_sorted_list(self):
        """
            Traverses tree and outputs all Nodes a sorted list. 
        
        Returns:
            list -- sorted list of strings to be outputted to csv file
        """
        all_nodes_as_dicts = []
        to_print = []
        # traverse tree
        for top_key in self._top_tree().keys():
            all_mid_keys = self._top_tree()[top_key]
            for mid_key in all_mid_keys:
                current_node = self._top_tree()[top_key][mid_key]
                all_nodes_as_dicts.append(current_node.as_dict())
        # sort
        all_nodes_as_dicts = sorted(all_nodes_as_dicts, key = lambda i: (i['date'], i['totalentries'], i['measure'], i['border']), reverse=True)

        # to print
        for node_dict in all_nodes_as_dicts:
            to_print.append(node_dict['border'] + ',' + 
                                 node_dict['date'] + ','  +
                                 node_dict['measure'] + ',' + 
                                 str(node_dict['totalentries']) + ',' +
                                 str(node_dict['runningaverage']))

        return (to_print)