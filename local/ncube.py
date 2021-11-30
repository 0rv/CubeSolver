# CMPT 417/427
# Rubiks Cube solving
# General cube class
# Ryan Vansickle

import numpy as np
# numpy arrays for column assignment

class nCube:
  # n = 0
  # dimensions of cube
  # 6 faces of cube, (F)ront (U)p (L)eft (B)ack (R)ight  (D)own
  

  # self.adj contains, in order:
  # the list of adjacent faces
  # the list of axes to take adjacents (1 = col, 0 = row)
  # list of if the adjacent row/col is the first or last indice
  # use this to index when rotating
  adj = {
    # adjacency data for calculating cube transforms
    # axis 0 = row, 1 = col
    #      faces                    axis           indices       CW flipmap     CCW flipmap
    'F': (['U', 'L', 'D', 'R'], [0, 1, 0, 1], [-1, -1,  0,  0], [1, 0, 1, 0], [0, 1, 0, 1]),
    'U': (['B', 'L', 'F', 'R'], [0, 0, 0, 0], [ 0,  0,  0,  0], [], []),
    'L': (['U', 'B', 'D', 'F'], [1, 1, 1, 1], [ 0, -1,  0,  0], [0, 1, 1, 0], [1, 1, 0, 0]),
    'B': (['U', 'R', 'D', 'L'], [0, 1, 0, 1], [ 0, -1, -1,  0], [], []),
    'R': (['U', 'F', 'D', 'B'], [1, 1, 1, 1], [-1, -1, -1,  0], [], []),
    'D': (['F', 'L', 'B', 'R'], [0, 0, 0, 0], [-1, -1, -1, -1], [], [])
  }
  
  def __str__(self):
    # sloppy implementation but it'll do
    if self.faces["F"] is None:
      return "nonecube %d"%(self.n)
    out = ("")
    for i in range(self.n):
      out += "U {}".format(self.faces['U'][i]) + " "*(7+2*(self.n)) + "D {}".format(self.faces['D'][i])+"\n"
    for i in range(self.n):
      out += "F {}".format(self.faces['F'][i]) + "  L {}".format(self.faces['L'][i]) + "  B {}".format(self.faces['B'][i]) + "  R {}".format(self.faces['R'][i]) + "\n"

      
    return out
    
  def __init__(self, data, n=3, path=None, depth=0):
    # data takes 6 nxn ndarrays of dtype int in a dict with keys FULBRD
    # not sanitizing input atm, dont be dumb
    # pass None to data for a solved cube
    self.n = n
    self.faces = {
      #shell of face data, 6x nxn numpy arrays
      'F': None,
      'U': None,
      'L': None,
      'B': None,
      'R': None,
      'D': None
    }
    
    self.n = n
    self.path = path
    self.depth = depth
    
    if path is None:
      self.path = []
    

    if data is None:
      # gives you an nxn of 1..6 (a solved cube of size n)
      data = [np.ones([n, n], dtype=int)*i for i in range(1, 7)]
    for key, i in zip(self.faces, range(6)):
      self.faces[key] = data[i]
      
      
  def data(self):
    return self.faces
  
  def path(self):
    return self.path
  
  def transform(self, face, dir):
    # takes a face (FULBRD) and direction (-1, 1)
    # 1 = CW, -1 = CCW (rot90 not intuitive we I swap)
    # returns the data
    # there is a mathematical way to do this and Im not sure what it is xd
    # doing this inefficiently (read: humanly parsable) for higher n
    
    if face not in ['F', 'U', 'L', 'B', 'R', 'D']:
      print("Error: invalid face in transform call: ", face)
    

    
    # rotate the face (easy part)
    self.faces[face] = np.rot90(self.faces[face], -dir)
    
    dats = np.zeros([4, self.n], dtype=int)
    # this will hold the list of 4 adjacwent rows/cols squeezed to format
    
    for i in range(4):
      #dats[i] = self.faces[face]
      
      dats[i] = self.faces[self.adj[face][0][i]].take( self.adj[face][2][i], self.adj[face][1][i])
    
    print(dats)
    dats = np.roll(dats, self.n)
    print('roll')
    print(dats)
# dcube = Cube(None)



# zero_faces = [np.zeros([3, 3], dtype=int)]*6
# zcube = Cube(zero_faces, 3)
# four_cube = Cube(None, 4)
# two_cube = Cube(None, 2)

# print(zcube)
# print(dcube)
# print(four_cube)
# print(two_cube)

# dcube.transform('F', 1)


# TEST DATA
# https://cube-solver.com/

# F U R https://puu.sh/IsD9r/3fbbf67842.png
# B D L https://puu.sh/IsDao/dc1931a214.png

# 1 = red
# 2 = yellow
# 3 = blue
# 4 = orange
# 5 = green
# 6 = white
dat = [
  np.array([[1, 6, 4], [4, 1, 6], [5, 1, 1]]), #F
  np.array([[5, 2, 5], [5, 6, 6], [2, 4, 2]]), #U
  np.array([[6, 6, 3], [1, 5, 3], [3, 1, 4]]), #L
  np.array([[4, 5, 1], [4, 4, 6], [5, 2, 4]]), #B
  np.array([[3, 4, 6], [3, 3, 2], [6, 5, 2]]), #R
  np.array([[2, 3, 3], [2, 2, 1], [6, 3, 1]])  #D
]

test = Cube(dat)
print(test)

print("transform('L', 1)")
test.transform('L', 1)


