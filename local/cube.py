# CMPT 417/427
# Rubiks Cube solving v2
# General cube class
# Ryan Vansickle

import numpy as np
# https://dl.acm.org/doi/10.1145/384283.801107
# https://medium.com/@benjamin.botto/implementing-an-optimal-rubiks-cube-solver-using-korf-s-algorithm-bf750b332cf9

class Cube:
  
  
  def __str__(self):
    if self.data is None:
      return "nonecube %d"%(self.n)
    out = ""
    for i in range(1,self.n+1):
      out += (" ")*(2+2*self.n) + "{}\n".format(self.data[:,0][i][1:-1])
    for i in range(1,self.n+1):
      out += "{} {} {} {}\n".format(self.data[:,:,0][i][1:-1], self.data[0][i][1:-1], self.data[:,:,-1][i][1:-1], self.data[-1][i][1:-1])
    for i in range(1,self.n+1):
      out += (" ")*(2+2*self.n) + "{}\n".format(self.data[:,-1][i][1:-1])
      
    return out
    
  def __init__(self, data, n=3):
    # still not sanitizing input - be sure to match n to the size of the cube (shape-2)
    
    self.n = n
    

    if data is None:
      # gives you an nxn of 1..6 (a solved cube of size n)
      data = np.zeros([n+2, n+2, n+2], dtype=int)
      data[0]       = np.pad(np.ones([n, n])*1, pad_width=1, mode='constant', constant_values=0) #F
      data[:,0]     = np.pad(np.ones([n, n])*2, pad_width=1, mode='constant', constant_values=0) #U
      data[:,:,0]   = np.pad(np.ones([n, n])*3, pad_width=1, mode='constant', constant_values=0) #L
      data[-1]      = np.pad(np.ones([n, n])*4, pad_width=1, mode='constant', constant_values=0) #B
      data[:,-1]    = np.pad(np.ones([n, n])*5, pad_width=1, mode='constant', constant_values=0) #D
      data[:,:,-1]  = np.pad(np.ones([n, n])*6, pad_width=1, mode='constant', constant_values=0) #R
      
      self.data = data
      # FIXME surely I can do this by going across axis 1:3???
      # doesnt need to be efficient, should only happen once per solve
      
  def transform(self, index, axis, dir):
    # index n indicates col or row to be rotated (1..n)
    # axis indicates row or column (0,1,2)
    # axis 0 is front-back
    # axis 1 is bottom-top
    # axis 2 is left-right
    # dir indicates CW or CCW - 90 or -90deg (-1, 1)
    print("transform on index {} axis {} dir {}".format(index, axis, dir))
    #print(self)
    #print(np.rot90(self.data.take(index, axis), dir ))
    print(self.data.take(index, axis) )

  
      
  def data(self):
    return self.data

  def is_solved(self):
    pass



dcube = Cube(None, 3)
print(dcube)

dcube.transform(1, 0, 1)



