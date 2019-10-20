#!/usr/bin/env python

from my_node import Node
from my_utils import myround

class Tree(object):
    """Tree objects are made of Node(s) stored in _nodes ."""

    def __init__(self):
        """
            Initiate a new tree.
        """
        #: dictionary, identifier: Node object
        self._nodes = {}
        self._add_root()
    
    def _add_root(self):
        self._nodes["ROOT"] = {}

    def _top_tree(self):
        return self._nodes["ROOT"]

    def _add_node_to_tree(self, top_key, mid_key, node):
        mid_tree = {}
        mid_tree[mid_key] = node
        self._top_tree()[top_key] = mid_tree

    def _update_node_to_tree(self, top_key, mid_key, node):
        self._top_tree()[top_key][mid_key] = node

    def add_node(self, node):

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
            # add nod
            else:
                self._update_node_to_tree(top_key, mid_key, node)
        else: 
            # brand new entry
            self._add_node_to_tree(top_key, mid_key, node)

    def add_averages(self):
        all_top_keys = self._top_tree().keys()
        for top_key in all_top_keys:
            # dates
            current_dates = self._top_tree()[top_key]

            # check if they can all be sorted?
            current_dates_list = sorted(current_dates, reverse=False)
            number_seen = 0
            running_total = 0
            prev_total = 0
            # loop through dates and make running average
            for current_date in current_dates_list:
                # running total
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

        # to Print
        for node_dict in all_nodes_as_dicts:
            to_print.append(node_dict['border'] + ',' + 
                                 node_dict['date'] + ','  +
                                 node_dict['measure'] + ',' + 
                                 str(node_dict['totalentries']) + ',' +
                                 str(node_dict['runningaverage']))

        return (to_print)