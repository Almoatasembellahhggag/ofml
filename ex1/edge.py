class Edge:

  def __init__(self, left,right,costs):
    self.left = left
    self.right = right
    self.costs = costs
  
  def get_Left(self):
    return self.left
    
  def get_Right(self):
    return self.right
    
  def get_Costs(self):
    return self.costs

  # setter method
    
  def set_right(self, x):
    self.right = x   
        
  def set_Left(self, x):
    self.left = x    
        
  def set_Costs(self, x):
    self.costs= x  
  
  def Print_edge(self):
    print('this is an edge left = {}, right = {}' .format(self.left,self.right))
    
  def reverse_edge(self):
    tmp = self.right
    self.right = self.left
    self.left = tmp
    new_costs = {}
    for i in range (int(len(self.costs) **0.5)):
      for j in range (int(len(self.costs)**0.5)):
        new_costs[(i,j)] = self.costs[(j,i)] 
    self.costs = new_costs


