# CMPT 417/427
# Rubiks Cube solving
# General cube class
# Ryan Vansickle

import numpy as np
# based on prelim research, standard python lists are
# actually faster than numpy here unless we go to big n
# but we use this for column assignments

class Cube:
  n = 0
  # dimensions of cube
  path = []
  # path to solution (if exists, to be passed to next search step instances)
  
  # 6 faces of cube, (F)ore (U)p (L)eft (B)ack (R)ight  (D)own
  # **ALWAYS** pass face data in FULBRD order (easy to rember, does a front/back ordering)
  F = None
  U = None
  L = None
  B = None
  R = None
  D = None
    
  
  def __str__(self):
    # sloppy implementation but it'll do
    if not self.F:
      return "nonecube %d"%(self.n)
    out = ("""\
    {} {} {}              {} {} {}
 U  {} {} {}            D {} {} {}
    {} {} {}              {} {} {}
    {} {} {}   {} {} {}   {} {} {}   {} {} {}
 F  {} {} {} R {} {} {} B {} {} {} L {} {} {}
    {} {} {}   {} {} {}   {} {} {}   {} {} {}""").format(
      
    )
    return 
    
  def __init__(self, data, n=3, path=[]):
    # data takes 6 nxn ndarrays in a list
    # not sanitizing input atm, dont be dumb
    # pass None to data for a solved cube
    
    self.n = n
    if not data:
      # gives you a 3x3 of 1..6 (a solved cube of size n)
      data = [i * np.ones([n, n]) for i in range(1, 7)]
    for i, face in enumerate([self.F, self.B, self.L, self.R, self.U, self.D]):
      face = data[i]
      
      
      
new = Cube(None)
print(new)
  
  
  










