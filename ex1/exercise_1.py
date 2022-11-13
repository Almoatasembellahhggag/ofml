#!/usr/bin/env python3
# This is the file where should insert your own code.
#
# Author: Your Name <your@email.com>
import numpy as np
import itertools
from collections import namedtuple


# For exercise 1.2
def evaluate_energy(nodes, edges, assignment):
    c = [node.costs for node in nodes]

    energy_node = 0
    for id, assign in enumerate(assignment):
         energy_node+=c[id][assign]
    
    energy_edge = 0
    for edge in edges:
        energy_edge+=edge.costs[(assignment[edge.left],assignment[edge.right])]

    return energy_node+energy_edge

# For exercise 1.3
def bruteforce(nodes, edges):
    assignment = [0] * len(nodes)
    # TODO: implement brute-force algorithm here...
    possibilities = []
    all_energy = []
    for node in nodes:
        p = [i for i in range(len(node.costs))]
        possibilities.append(p)
    assignments = list(itertools.product(*possibilities))
    for assignment in assignments:
        energy = evaluate_energy(nodes, edges, assignment)
        all_energy.append(energy)
        
    return (assignments[np.argmin(all_energy)], np.min(all_energy))


# For exercise 1.4


def dynamic_programming(nodes, edges):
    
    # make sure that i only use the edges that would make the a chain (right = left - 1) 
    new_edges = [edge for edge in edges if (edge.right - edge.left == 1)]
    
    #Processed label is a named tuple (pseudo object) that i created to store the date of each label ( (F) , Unary cost (Theta) , connected label (to get the back tracing))
    processed_label = namedtuple('processed_label', 'F unary_cost connected_label')
    
    #Processed node is a named tuple (pseudo object) that i created to store the list of processed labels in each node)
    processed_node = namedtuple('processed_node', 'processed_labels')    
    
    #list of all processed nodes
    processed_nodes = []    

    for index , node in enumerate(nodes):
        list_of_processed_labels = []

        #for the first node all the labels in the node will have F = 0 - given in the lecture - and each label won't be conected to other nodes from the left (because it is the first node in the chain) 
        
        if (index == 0):
            for i,cost in enumerate(node.costs):
              new_label = processed_label(F=0,unary_cost=node.costs[i],connected_label=None)
              list_of_processed_labels.append(new_label)
            curr_node = processed_node(processed_labels=list_of_processed_labels)
            processed_nodes.append(curr_node)

        else:
            for curr_index,curr_label_cost in enumerate (node.costs):
                comparision_array = []
                for prev_index,prev_label in enumerate (processed_nodes[index-1].processed_labels):
                     # sum unary cost and F of ( modified node[0]) + the pairwise cost (the corresbonding edge)
                     value = prev_label.F + prev_label.unary_cost + new_edges[index-1].costs[(prev_index,curr_index)]
                     comparision_array.append(value)
                     
                new_label = processed_label(F=np.min(comparision_array),unary_cost=curr_label_cost,connected_label=np.argmin(comparision_array))
                list_of_processed_labels.append(new_label)
            curr_node = processed_node(processed_labels=list_of_processed_labels) 
            processed_nodes.append(curr_node)

            if index == len(nodes)-1:
                last_node_comparision_array =[]
                for label in curr_node.processed_labels:
                    last_node_comparision_array.append((label.unary_cost+label.F))
                ptr = np.argmin(last_node_comparision_array)
                
    print([ label.F+label.unary_cost for label in processed_nodes[-1].processed_labels])  
    return processed_nodes, ptr

def backtrack(nodes, edges, processed_nodes, ptr):
    
    processed_nodes = list(reversed(processed_nodes))
    assignment=[ptr]    
    for index,node in enumerate(processed_nodes):
        next_step = node.processed_labels[assignment[-1]].connected_label
        if (next_step !=None):
            assignment.append(next_step)

             
    return list(reversed(assignment))


# For exercise 1.5
def compute_min_marginals(nodes, edges):

    processed_nodes_forward,first_step = (dynamic_programming(nodes, edges))

    processed_nodes_backward,firstt_step = list(reversed (dynamic_programming(list(reversed(nodes)), edges) ))
    
    m = np.zeros((len(nodes),len(nodes)))

    for index , forward_node in enumerate(processed_nodes_forward):
        for index2 , label in enumerate(forward_node.processed_labels):
            m[index][index2] = label.unary_cost + label.F + processed_nodes_backward[index].processed_labels[index2]






    
    print(m)
    return m


# For execrise 1.6
def dynamic_programming_tree(nodes, edges):
    F, ptr = None, None
    return F, ptr

def backtrack_tree(nodes, edges, F, ptr):
    assignment = [0] * len(nodes)
    return assignment
