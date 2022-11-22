import numpy as np
from label import Label
class Node:
    

  def __init__(self,node_id,costs,edges,F,B=[]):
      
    self.node_id= node_id
    self.costs = costs
    self.F = F 
    self.B = B
    connected_nodes = ([edge.right for edge in edges if edge.get_Left() == node_id] + [edge.left for edge in edges if edge.get_Right() == node_id ])
    connected_nodes.sort()
    self.connected_nodes = (connected_nodes)
    self.connected_node = self.connected_nodes[0] if len(self.connected_nodes)==1 else None
    self.connected_edges =  [edge for edge in edges if (edge.get_Left() == node_id or edge.get_Right() == node_id)] 
    self.connected_edge = self.connected_edges[0]if len(self.connected_edges)==1 else None
    self.leaf = True if (len ( self.connected_edges ) == 1) else False

  

  def get_costs(self):
    return self.costs

  def is_a_a_leaf(self):
    return self.leaf

  def is_connected_from_right(self):
    return self.leaf_connected_from_right
    
  def get_node_id(self):
    return self.node_id
    
  def get_F(self):
    return self.F
    
  def get_B(self):
    return self.B
    
  def get_Conected_nodes(self):
    return self.Conected_nodes
    
  def get_connected_edges(self):
    return self.connected_edges
  
  def get_connected_edge(self):
    return self.connected_edge 
  
  def get_Conected_node(self):
    return self.connected_node   


    
    # setter methods
      

  def set_costs(self, x):
    self.costs = x    
        
  def set_F(self, x):
    self.F = x    
        
  def set_B(self, x):
    self.B= x    

  def print_node(self):
    #print('this is a node no : {},  unerary costs = {}, F = {}, B = {}, Connected eges are {}, and connected Nodes are {} '.format(self.node_id,[ label.get_unary_cost() for label in self.costs ],self.F,self.B,len(self.connected_edges),self.connected_nodes))
     print (' this is node no :{} it is connected to {}'.format(self.node_id,self.connected_nodes))
     
  def calculate(self,node,right_or_left):
      labels =[]
      for curr_index,curr_label in enumerate(self.get_costs()):
          comparision_array=[]
          for prev_index,prev_label in enumerate(node.get_costs()):
              comparision_array.append( curr_label.get_F() + prev_label.get_F() + node.get_connected_edge().get_Costs()[(prev_index,curr_index) if  right_or_left  else (curr_index,prev_index)] )
          min = np.min(comparision_array)
          curr_label.set_F(min)
          curr_label.set_connected_label(node.get_costs()[np.argmin(comparision_array)])
          curr_label.set_connected_node(node)
          
          labels.append(curr_label)
      self.F = [label.get_F() for label in labels]
      self.set_costs (labels)     
          
              
              
  def reset(self, edges):
      
      connected_nodes = ([edge.right for edge in edges if edge.left == self.node_id] + [edge.left for edge in edges if edge.right == self.node_id ])
      connected_nodes.sort()
      self.connected_nodes = (connected_nodes)
      self.connected_node = self.connected_nodes[0] if len(self.connected_nodes)==1 else None
      self.connected_edges =  [edge for edge in edges if (edge.left == self.node_id or edge.right == self.node_id)] 
      self.connected_edge = self.connected_edges[0] if len(self.connected_edges)==1 else None
      self.leaf = True if (len ( self.connected_edges ) == 1) else False
  
          

    

