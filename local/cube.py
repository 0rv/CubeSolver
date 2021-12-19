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
      face = np.ones([n, n])
      data[0]       = np.pad(face*1, pad_width=1, mode='constant', constant_values=0) #F
      data[:,0]     = np.pad(face*2, pad_width=1, mode='constant', constant_values=0) #U
      data[:,:,0]   = np.pad(face*3, pad_width=1, mode='constant', constant_values=0) #L
      data[-1]      = np.pad(face*4, pad_width=1, mode='constant', constant_values=0) #B
      data[:,-1]    = np.pad(face*5, pad_width=1, mode='constant', constant_values=0) #D
      data[:,:,-1]  = np.pad(face*6, pad_width=1, mode='constant', constant_values=0) #R
      
    self.data = data
      # FIXME surely I can do this by going across axis 1:3???
      # doesnt need to be efficient, should only happen once per solve
      
    
  def transform(self, index, axis, dir):
    # axis indicates row or column (0,1,2)
    
    # axis 0 is front-back
    # axis 1 is bottom-top
    # axis 2 is left-right
    
    # index n indicates col or row to be rotated (1..n)
    # axis indicates row or column (0,1,2)
    # dir indicates CW or CCW; 90 or -90deg (-1, 1)
    # print("transform on axis {} index {} dir {}".format(axis, index, dir))
    
    t = [
      (index),
      (slice(None), index),
      (slice(None), slice(None), index)
    ]
    self.data[t[axis]] = np.rot90(self.data.take(index, axis), dir)
    
    if (index == self.n):
      # if rotating an edge piece, we must also rotate the shell layer
      index+=1
      t = [
        (index),
        (slice(None), index),
        (slice(None), slice(None), index)
      ]
      self.data[t[axis]] = np.rot90(self.data.take(index, axis), dir)
      
    if (index == 1):
      # edge piece
      index=0
      t = [
        (index),
        (slice(None), index),
        (slice(None), slice(None), index)
      ]
      # tmp = np.rot90(self.data.take(index, axis), dir)
      self.data[t[axis]] = np.rot90(self.data.take(index, axis), dir)
  

  def solved(self):
    flag = True
    for x in [self.data[0], self.data[-1], self.data[:,0], self.data[:,-1], self.data[:,:,0], self.data[:,:,-1]]:
      # for each outer face
      flag = (len(np.unique(x))==2 and flag)
    return flag
  

  def draw3(self):
    # # # DISPLAY # # #
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    # THIS FUNCTION WILL BE SLOW AF SORRY
    # 1 = WHITE
    # 2 = ORANGE
    # 3 = GREEN
    # 4 = YELLOW
    # 5 = RED
    # 6 = BLUE
    alpha = 0.9
    
    colours = [
      [0, 0, 0, 0.0],
      [1, 1, 1, alpha],
      [1, .5, 0, alpha],
      [0, 1, 0, alpha],
      [1, 1, 0, alpha],
      [1, 0, 0, alpha],
      [0, 0, 1, alpha]
    ]
    
    
    coldat = np.zeros([self.n+2, self.n+2, self.n+2, 4])
    for index, x in np.ndenumerate(self.data):
      coldat[index] = colours[x]
    
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.voxels(self.data, facecolors=coldat, edgecolors='grey')
    plt.show()










