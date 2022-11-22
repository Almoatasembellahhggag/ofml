

class Label:

  def __init__(self,label_index,node_id ,unary_cost,B=0,connected_label=None,connected_node=None):
    self.node_id = node_id 
    self.label_index = label_index 
    self.unary_cost = unary_cost
    self.F = unary_cost
    self.B = B
    self.connected_label = connected_label
    self.connected_node = connected_node


# getter method
    
  def get_unary_cost(self):
    return self.unary_cost
    
  def get_F(self):
    return self.F
    
  def get_B(self):
    return self.B
    
  def get_connected_label(self):
    return self.connected_label
    
  def get_connected_node(self):
    return self.connected_node
  
  def get_index(self):
    return self.label_index
    
    
  # setter method
    
  def set_unary_cost(self, x):
    self.unary_cost = x    
        
  def set_F(self, x):
    self.F = x    
        
  def set_B(self, x):
    self.B= x    

  def set_connected_label(self, x):
    self.connected_label = x    
        
  def set_connected_node(self, x):
    self.connected_node = x    
    
  def Print_Label(self):
    print ('this is label no {} in node with Id = {}, the unary cost of this label = {}, the F value = {}, The B value = {}, this label is connected to lABEL no {} in Node with Id = {}'.format(self.label_index,self.node_id,self.unary_cost,self.F,self.B,self.connected_label,self.connected_node))

 
 
 



